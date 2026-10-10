"""Rebuild static graph, evidence indexes and exports from retained extraction.

Never runs Pi, its tests, a model, or a network request. Writes only graphify-out.
"""
import hashlib
import importlib.metadata
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json, to_html, to_obsidian, attach_hyperedges
from graphify.diagnostics import diagnose_extraction, format_diagnostic_report
from graphify.detect import save_manifest
from graphify.cache import save_semantic_cache
from graphify.cli import _stamped_manifest_files
from graphify.benchmark import run_benchmark, print_benchmark

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'graphify-out'
SPEC = Path('/Users/jason/.codex/skills/graphify/references/extraction-spec.md')
EXPECTED = 'cd32f7725fdbddbaecdff5b1e68491563394e0ca'

def read(name):
    return json.loads((OUT / name).read_text(encoding='utf-8'))

def write(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def relative(path):
    if not path:
        return ''
    p = Path(path)
    if p.is_absolute():
        try:
            return str(p.relative_to(ROOT))
        except ValueError:
            return str(p)
    return str(p)

def symbol_nodes(nodes, path, symbols):
    matches = []
    for n in nodes:
        if relative(n.get('source_file')) != path:
            continue
        label = n.get('label','')
        if any(label == s or label == s+'()' or label.endswith('.'+s+'()') for s in symbols):
            matches.append(n['id'])
    return sorted(set(matches))

def main():
    os.chdir(ROOT)
    revision = subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
    if revision != EXPECTED:
        raise SystemExit('Revision changed. Review evidence before rebuilding.')
    detection = read('.graphify_detect.json') if (OUT/'.graphify_detect.json').exists() else read('corpus.json')
    ast = read('.graphify_ast.json') if (OUT/'.graphify_ast.json').exists() else read('structural-extraction.json')
    write('corpus.json',detection)
    write('structural-extraction.json',ast)
    fragments = sorted(OUT.glob('.graphify_chunk_*.json'))
    if fragments:
        if len(fragments) != len(read('semantic-batches.json')):
            raise SystemExit('Incomplete semantic batches: refusing partial graph overwrite.')
        semantic = {'nodes':[],'edges':[],'hyperedges':[],'input_tokens':0,'output_tokens':0}
        for path in fragments:
            chunk = json.loads(path.read_text())
            ids = {n['id'] for n in chunk['nodes']}
            assert len(ids)==len(chunk['nodes']), f'duplicate node ID in {path}'
            for edge in chunk['edges']:
                assert edge['source'] in ids and edge['target'] in ids, f'dangling {path}'
                assert edge['confidence_score'] is not None
            for key in ('nodes','edges','hyperedges'):
                semantic[key] += chunk.get(key,[])
        write('semantic-extraction.json',semantic)
        allowed=[f for cat in ('document','paper','image') for f in detection['files'].get(cat,[])]
        print('Semantic files cached:',save_semantic_cache(semantic['nodes'],semantic['edges'],semantic['hyperedges'],root=ROOT,cache_root=ROOT,allowed_source_files=allowed,prompt_file=SPEC),flush=True)
    else:
        semantic=read('semantic-extraction.json')

    # Index containment is explicitly tagged; it is not an execution edge.
    nodes={n['id']:dict(n) for n in ast['nodes']}
    for n in semantic['nodes']:
        nodes.setdefault(n['id'],dict(n))
    edges=[dict(e) for e in ast['edges']+semantic['edges']]
    for edge in edges:
        edge.setdefault('confidence_score',1.0 if edge.get('confidence')=='EXTRACTED' else None)
        edge.setdefault('evidence_category','structure_extracted' if edge.get('_origin')=='ast' else 'document_semantics')
    file_nodes={relative(n.get('source_file')):n['id'] for n in nodes.values() if n.get('label')==Path(n.get('source_file') or '').name}
    for cat in ('document','paper','image'):
        for f in detection['files'].get(cat,[]):
            rel=relative(f)
            fid='index_file_'+re.sub(r'[^a-z0-9]','_',rel.lower())
            nodes.setdefault(fid,{'id':fid,'label':Path(f).name,'file_type':cat,'source_file':rel,'source_location':None,'evidence_category':'index_membership'})
            file_nodes[rel]=fid
            for n in semantic['nodes']:
                if relative(n.get('source_file'))==rel:
                    edges.append({'source':fid,'target':n['id'],'relation':'contains','confidence':'EXTRACTED','confidence_score':1.0,'source_file':rel,'source_location':n.get('source_location'),'evidence_category':'index_membership','weight':1.0})

    evidence=read('evidence-seed.json')
    for item in evidence['claims']:
        source=ROOT/item['source_file']
        content=source.read_text(encoding='utf-8')
        for symbol in item['symbols']:
            assert symbol in content,(item['id'],symbol)
        item['source_sha256']=digest(source)
        item['graph_node_ids']=symbol_nodes(list(nodes.values()),item['source_file'],item['symbols'])
        item['source_excerpt']=[{'symbol':s,'text':'\n'.join(content.splitlines()[max(0,next(i for i,l in enumerate(content.splitlines()) if s in l)-1):next(i for i,l in enumerate(content.splitlines()) if s in l)+4])} for s in item['symbols']]
        item['revision']=revision
        item['runtime_observed']=False
        nid='evidence_'+item['id'].lower()
        nodes[nid]={'id':nid,'label':item['id']+' '+item['claim'],'file_type':'rationale','source_file':item['source_file'],'source_location':', '.join(item['symbols']),'evidence_category':item['category'],'evidence_id':item['id'],'condition':item['condition']}
        targets=item['graph_node_ids'] or [file_nodes.get(item['source_file'])]
        for target in targets:
            if target:
                edges.append({'source':nid,'target':target,'relation':'references','confidence':'INFERRED' if item['category']=='semantic_inference' else 'EXTRACTED','confidence_score':0.85 if item['category']=='semantic_inference' else 1.0,'source_file':item['source_file'],'source_location':', '.join(item['symbols']),'evidence_category':item['category'],'evidence_id':item['id'],'weight':1.0})
    # Package manifest relationships. No package containment is used as a call edge.
    packages=[]
    for manifest in sorted((ROOT/'packages').glob('*/package.json')):
        d=json.loads(manifest.read_text())
        packages.append({'directory':manifest.parent.name,'name':d['name'],'version':d.get('version'),'description':d.get('description'),'dependencies':d.get('dependencies',{}),'source_file':relative(manifest),'sha256':digest(manifest)})
    name_to_id={p['name']:'package_'+p['directory'].replace('-','_') for p in packages}
    for package in packages:
        pid=name_to_id[package['name']]
        nodes[pid]={'id':pid,'label':package['name'],'file_type':'concept','source_file':package['source_file'],'source_location':'package.json: name/dependencies','evidence_category':'structure_extracted'}
        for dep in package['dependencies']:
            if dep in name_to_id:
                edges.append({'source':pid,'target':name_to_id[dep],'relation':'depends_on','confidence':'EXTRACTED','confidence_score':1.0,'source_file':package['source_file'],'source_location':'dependencies','evidence_category':'manifest_dependency','weight':1.0})
        prefix='packages/'+package['directory']+'/'
        for path,fid in file_nodes.items():
            if path.startswith(prefix):
                edges.append({'source':pid,'target':fid,'relation':'contains','confidence':'EXTRACTED','confidence_score':1.0,'source_file':path,'source_location':None,'evidence_category':'index_membership','weight':1.0})

    extraction={'nodes':list(nodes.values()),'edges':edges,'hyperedges':semantic.get('hyperedges',[]),'input_tokens':0,'output_tokens':0,'token_usage_status':'unknown; host/subagent usage unavailable','revision':revision}
    write('extraction.json',extraction)
    health=diagnose_extraction(extraction,directed=True,root=str(ROOT))
    write('graph-health.json',health)
    print(format_diagnostic_report(health),flush=True)
    G=build_from_json(extraction,root=str(ROOT),directed=True)
    assert G.number_of_nodes()>0,'Empty graph'
    attach_hyperedges(G,extraction['hyperedges'])
    print(f'Clustering {G.number_of_nodes()} nodes...',flush=True)
    communities=cluster(G)
    cohesion=score_all(G,communities)
    labels={}
    names={'agent':'Agent 控制循环','ai':'AI 模型协议','coding-agent':'Coding Agent 会话工具','chord':'Chord 服务状态','durable':'Durable 持久任务','tui':'TUI 终端组件','mcp':'MCP 远端工具','codemode':'Codemode 沙箱执行','protocol':'Protocol 传输协议','client':'Client 远程连接','server':'Server 会话路由','evals':'Evals 行为评估','telemetry':'Telemetry 遥测契约'}
    for cid,members in communities.items():
        counts=Counter()
        for nid in members:
            path=G.nodes[nid].get('source_file','') or ''
            parts=Path(path).parts
            if len(parts)>1 and parts[0]=='packages': counts[parts[1]]+=1
        dominant=counts.most_common(1)
        name=names.get(dominant[0][0],'仓库 构建维护') if dominant else '跨包 类型基础'
        labels[cid]=f'{name} {cid}'
    # Structured learning navigation complements heuristic structural communities.
    qmap={1:['E14','E18'],2:['E08','E09','E15','E27'],3:['E03','E05','E10'],4:['E13','E16'],5:['E06','E07','E17','E23'],6:['E15','E20','E21','T06'],7:['E04','E11','E28'],8:['E18','E20','E22','E24'],9:['E01','E02','E04','E26','I01'],10:['E13','E25','E29']}
    byid={i['id']:i for i in evidence['claims']}
    questions=[]
    for q,ids in qmap.items():
        questions.append({'id':f'Q{q}','question_anchor':f'learning-questions.md#q{q}','explanation':'core-flow.md' if q!=9 else 'architecture.md','evidence_ids':ids,'sources':[{'source_file':byid[i]['source_file'],'symbols':byid[i]['symbols'],'graph_node_ids':byid[i]['graph_node_ids']} for i in ids]})
    write('question-index.json',{'revision':revision,'questions':questions})
    steps=[('input','终端输入进入会话','E03','InteractiveMode 输入队列'),('prompt','会话前置处理与消息构造','E10','AgentSession'),('loop','运行快照与循环开始','E05','Agent activeRun / loop currentContext'),('declarations','工具声明delta','E11','transcript / executable tools'),('projection','请求前从原始记录投影','E08','SessionManager'),('request','上下文变换并交给模型','E09','loop / ModelRuntime'),('response','流式形成assistant调用','E12','loop partial / Agent streamingMessage'),('dispatch','工具准备和调度','E13','loop prepared outcome'),('read','默认本地read操作','E14','ReadOperations'),('result','工具消息与错误封装','E18','loop ToolResultMessage'),('continue','回填与下一轮判断','E15','loop currentContext / 队列'),('end','等待订阅者并idle','E20','Agent'),('settle','会话重试或收束','E21','AgentSession')]
    overlay={'revision':revision,'kind':'source-confirmed static walkthrough','runtime_observed':False,'steps':[{'id':k,'label':label,'evidence_id':e,'state_owner':owner,'graph_node_ids':byid[e]['graph_node_ids']} for k,label,e,owner in steps],'event_connections':[{'from':'Agent.processEvents','to':'AgentSession._handleAgentEvent','when':'await each Agent subscriber; append at message_end','evidence_ids':['E07','E17']},{'from':'AgentSession._emit','to':'InteractiveMode.handleEvent','when':'public notification; returned promise not awaited by _emit','evidence_ids':['E03','E17']}],'branches':{'missing_file':['E14','E18','T02'],'truncated_tool_call':['E16','T07'],'model_error':['E16','E20','E22'],'abort':['E24'],'next_turn_refresh':['E19']}}
    write('learning-overlay.json',overlay)
    gods=god_nodes(G)
    surprises=surprising_connections(G,communities)
    auto_questions=[{'type':'reviewed_learning_flow','question':'工具结果怎样跨过循环、事件订阅和会话投影，进入下一次模型请求？','why':'经源码核对的跨层连接；先做Q2预测，再查E08/E09/E15/E17/E27。'}]+suggest_questions(G,communities,labels)
    analysis={'communities':{str(k):v for k,v in communities.items()},'cohesion':cohesion,'labels':labels,'label_method':'deterministic dominant package; Chinese responsibility names; IDs distinguish groups','gods':gods,'surprises':surprises,'questions':auto_questions}
    write('analysis.json',analysis)
    write('.graphify_labels.json',{str(k):v for k,v in labels.items()})
    wrote=to_json(G,communities,str(OUT/'graph.json'),community_labels=labels,built_at_commit=revision,original_links=edges)
    if not wrote: raise SystemExit('Refused graph shrink; no report/export overwritten.')
    report=generate(G,communities,cohesion,labels,gods,surprises,detection,{'input':0,'output':0},str(ROOT),suggested_questions=auto_questions,built_at_commit=revision,obsidian=True)
    report=re.sub(r'^- Token cost:.*$', '- Token cost: UNKNOWN input/output; host and subagent usage are not exposed. AST requires no model tokens; schema zero counters are placeholders, not measured zero consumption.',report,flags=re.M)
    report+='\n\n## 本轮中文审计补充\n\n全仓静态结构提取 + 文档/图片语义概览 + 核心主链局部源码核对。未运行 Pi、测试、模型替身或真实模型。\n\n'
    report+='有方向的 graph.json 保留原始关系列表；聚类内部使用无方向投影。社区名称按主要包职责生成，不是逐社区人工行为审计。高连接节点/跨社区边不等同于关键运行路径。主链以 learning-overlay.json 和 evidence-index.json 为准。\n\n'
    report+='GRAPH HEALTH: '+json.dumps(health,ensure_ascii=False)+'\n\n'
    report+='关系折叠影响 NetworkX 简单图和社区/排名视图；extraction.json 保留全部原始边，graph.json保留端点已解析的多关系。折叠、自环与AST语法/无符号缺口需查 coverage.json，不能当作已完全解析的调用图。\n\n'
    report+='最值得继续的问题：**工具结果怎样跨过循环、事件订阅和会话投影，进入下一次模型请求？** 见 Q2、E08/E09/E15/E17/E27。\n'
    (OUT/'GRAPH_REPORT.md').write_text(report,encoding='utf-8')
    write('evidence-index.json',evidence)
    evidence_md=['# 论断与证据','',f'版本 `{revision}`。源码确认是局部静态阅读；测试只表达作者预期，全部未运行。源码导航使用文件/符号，不依赖行号。','']
    for item in evidence['claims']:
        evidence_md += [f'## {item["id"]}','',item['claim'],'',f'- 类别：`{item["category"]}`；条件：{item["condition"]}',f'- 源码：[{item["source_file"]}](../{item["source_file"]})',f'- 符号：'+', '.join('`'+s+'`' for s in item['symbols']),f'- 图节点：'+(', '.join('`'+n+'`' for n in item['graph_node_ids']) or '未获精确符号节点；使用文件/证据节点导航'),'']
    (OUT/'evidence.md').write_text('\n'.join(evidence_md),encoding='utf-8')

    source_confirmed=defaultdict(list)
    for item in evidence['claims']:
        source_confirmed[item['source_file']].append(item['id'])
    semantic_coverage={}
    for name in ('semantic-coverage-a.json','semantic-coverage-b.json','semantic-coverage-images.json'):
        cv=read(name)
        for item in cv.get('files',cv.get('images',[])):
            semantic_coverage[relative(item['source_file'])]=item
    node_sources=Counter(relative(n.get('source_file')) for n in ast['nodes'] if n.get('label')!=Path(n.get('source_file') or '').name)
    inventory=[]
    for category,files in detection['files'].items():
        for file in files:
            rel=relative(file)
            inventory.append({'path':rel,'category':category,'sha256':digest(file),'ast_attempted':category=='code','ast_symbol_node_count':node_sources[rel] if category=='code' else None,'semantic_node_count':sum(relative(n.get('source_file'))==rel for n in semantic['nodes']),'semantic_reading':semantic_coverage.get(rel),'source_review_evidence_ids':source_confirmed.get(rel,[]),'review_depth':'targeted_source_review' if rel in source_confirmed else 'structural_only' if category=='code' else 'semantic_overview','runtime_verified':False})
    coverage={'revision':revision,'total_detected':detection['total_files'],'total_words':detection['total_words'],'categories':{k:len(v) for k,v in detection['files'].items()},'files':inventory,'excluded':{k:[relative(x) for x in detection.get(k,[])] for k in ('skipped_sensitive','unclassified','ignored','pruned_noise_dirs','walk_errors')},'structural_failures':ast.get('failed_sources',[]),'parser_warnings':[{'path':'packages/tui/test/latex.test.ts','first_parser_error_line':220,'symbols_extracted':2,'meaning':'Tree-sitter parser diagnostic; not a TypeScript compiler failure; file partially extracted'},{'zero_symbol_files_reported_by_extractor':215,'meaning':'Data/barrel files or unsupported symbol forms; detected does not imply symbol completeness'}],'entry_only_branches':['compaction','steering/follow-up full variations','provider wire/caching/continuation','MCP/codemode algorithms','durable Harness','remote client/server lifecycle','TUI internals'],'health':health}
    write('coverage.json',coverage)
    provenance={'schema_version':1,'revision':revision,'product_version':'1.0.2','date_utc':datetime.now(timezone.utc).isoformat(),'root':str(ROOT),'python':sys.executable,'graphify_version':importlib.metadata.version('graphifyy'),'extraction_spec_sha256':digest(SPEC),'skill_path':'/Users/jason/.codex/skills/graphify/SKILL.md','plan_sha256':digest(OUT/'PLAN.md'),'packages':packages,'initial_git_status':' M .gitignore','current_git_status':subprocess.check_output(['git','status','--short'],text=True),'scope':'full repo supported static corpus; exclusions listed in coverage','directed':True,'clustering':'graphify cluster converts directed graph to undirected view','token_usage':{'input_tokens':None,'output_tokens':None,'status':'unavailable from host/subagent tools; zero fragment counters are placeholders'},'runtime_actions':{'pi_run':False,'tests_run':False,'faux_model_run':False,'provider_request':False},'tool_adaptations':['large-corpus warning surfaced; user plan already requires full repository','3 semantic workers sequentially process 13 chunks due 4-slot limit','fragments written under graphify-out and host-validated instead of inline JSON','AST parallel=False to avoid multiprocessing relaunch','retained extraction and analysis support static rebuild; raw relationships preserved','Obsidian and HTML exports requested by plan','community labels use package responsibility names; heuristic groups remain separate from reviewed flow'],'source_navigation_tools':['WebStorm MCP search_symbol/read_file/analyze_calls','local source reads to supplement limited/truncated IDE output and incomplete mapped dependency call tree'],'generation_relations':{'graph.json':['extraction.json','analysis.json'],'graph.html':['graph.json','analysis.json'],'obsidian/graph':['graph.json','analysis.json'],'obsidian/learning':['Chinese Markdown maintenance sources','export-learning.py'],'evidence.md':['evidence-index.json']}}
    write('provenance.json',provenance)
    stamped=_stamped_manifest_files(detection['files'],extraction,ROOT)
    save_manifest(stamped,root=ROOT,scan_corpus={f for files in detection['files'].values() for f in files})
    if not (OUT/'cost.json').exists():
        write('cost.json',{'runs':[{'date':provenance['date_utc'],'files':detection['total_files'],'input_tokens':None,'output_tokens':None,'usage_status':'unknown','ast_model_tokens':0}],'total_input_tokens':None,'total_output_tokens':None,'usage_status':'unknown; do not sum placeholder zero counters'})
    print(f'Graph {G.number_of_nodes()} nodes / {len(edges)} raw edges / {G.number_of_edges()} simple edges / {len(communities)} communities',flush=True)
    print('WARNING: >5000 nodes; HTML uses an aggregated community view; graph.json retains symbol-level detail.',flush=True)
    if not to_html(G,communities,str(OUT/'graph.html'),community_labels=labels,node_limit=5000):
        raise SystemExit('HTML export skipped unexpectedly.')
    print('Obsidian notes:',to_obsidian(G,communities,str(OUT/'obsidian'/'graph'),community_labels=labels,cohesion=cohesion),flush=True)
    bench=run_benchmark(str(OUT/'graph.json'),corpus_words=detection['total_words'],questions=['streamAssistantResponse createToolResultMessage','AgentSession prepareRequest buildSessionProjection','Agent agent_end agent_settled'])
    write('benchmark.json',bench)
    print_benchmark(bench)

if __name__ == '__main__':
    main()
