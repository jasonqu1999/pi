"""Derive Obsidian learning views and clickable source links, without Pi execution."""
import json
import os
import re
from pathlib import Path
from urllib.parse import quote, unquote

OUT=Path(__file__).resolve().parent
ROOT=OUT.parent
VAULT=OUT/'obsidian'

def put(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text,encoding='utf-8')

def rewrite_link(match,target_dir):
    label,target=match.groups()
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'):
        return match.group(0)
    file,sep,anchor=target.partition('#')
    file=unquote(file)
    source=(OUT/file).resolve()
    if file.endswith('.md') and source.parent==OUT and file!='PLAN.md':
        dest=VAULT/'learning'/file
    else:
        dest=source
    rel=Path(os.path.relpath(dest,target_dir)).as_posix()
    return f'[{label}]({quote(rel,safe="/._-")}{sep}{anchor})'

def main():
    graph=json.loads((OUT/'graph.json').read_text())
    provenance=json.loads((OUT/'provenance.json').read_text())
    raw=json.loads((OUT/'extraction.json').read_text())
    accounting={'raw_extraction_edges':len(raw['edges']),'exported_relationships':len(graph['links']),'net_count_difference':len(raw['edges'])-len(graph['links']),'graph_nodes':len(graph['nodes']),'raw_nodes':len(raw['nodes']),'note':'Graphify canonicalizes aliases/adds reference endpoints; JSON exporter retains multiple relationships only when both post-build endpoints exist. Extraction preserves raw data.'}
    put(OUT/'edge-export-gaps.json',json.dumps(accounting,ensure_ascii=False,indent=2))
    report_path=OUT/'GRAPH_REPORT.md'
    report=report_path.read_text()
    report=report.replace('extraction.json 与 graph.json 保留原始边','extraction.json 保留全部原始边，graph.json仅保留端点已解析的多关系')
    report=report.replace('Run `graphify update .` after code changes (no API cost).','源码变更后使用graphify skill更新并重核证据；文档语义提取token用量仍须单独记录。')
    # Link community hubs to actual exported notes instead of bare wiki names outside a vault.
    def community_link(m):
        stem,label=m.groups()
        target=OUT/'obsidian'/'graph'/(stem+'.md')
        return '['+label+']('+quote(str(target.relative_to(OUT)),safe='/._-')+')' if target.exists() else m.group(0)
    report=re.sub(r'\[\[([^]|]+)\|([^]]+)\]\]',community_link,report)
    if 'reviewed_learning_flow' not in report and '## Suggested Questions\n_Questions' in report:
        report=report.replace('## Suggested Questions\n_Questions this graph is uniquely positioned to answer:_','## Suggested Questions\n<!-- reviewed_learning_flow -->\n- **工具结果怎样跨过循环、事件订阅和会话投影，进入下一次模型请求？**\n  _经源码核对的跨层连接；先做Q2预测，再查E08/E09/E15/E17/E27。_\n\n_Questions this graph is uniquely positioned to answer:_')
    marker='## 关系导出对账'
    if marker in report: report=report.split(marker)[0].rstrip()
    report+='\n\n'+marker+'\n\n'+json.dumps(accounting,ensure_ascii=False)+'\n'
    put(report_path,report)
    coverage=json.loads((OUT/'coverage.json').read_text())
    coverage['export_accounting']=accounting
    coverage['external_module_references']=[{'id':n['id'],'source_file':n.get('source_file')} for n in graph['nodes'] if n.get('source_file') and not (ROOT/n['source_file']).exists()]
    coverage['reference_nodes_without_source']=sum(not n.get('source_file') for n in graph['nodes'])
    put(OUT/'coverage.json',json.dumps(coverage,ensure_ascii=False,indent=2))
    generated=[]
    names=['README.md','architecture.md','core-flow.md','source-navigation.md','learning-questions.md','expansion-backlog.md','evidence.md','GRAPH_REPORT.md','rebuild.md']
    for name in names:
        source=OUT/name
        dest=VAULT/'learning'/name
        content=source.read_text()
        content=re.sub(r'(?<!!)\[([^\]]*)\]\(([^)]+)\)',lambda m:rewrite_link(m,dest.parent),content)
        put(dest,'<!-- Derived from graphify-out/'+name+'; edit the Markdown source and re-export. -->\n\n'+content)
        generated.append({'target':str(dest.relative_to(OUT)),'source':name})
    put(VAULT/'学习入口.md','''# Pi 1.0.2 学习入口

新会话里输入「总结 notes.md」。假设模型先返回 read 调用，再回答：**文件正文第一次出现在哪里？下次请求怎样得到它？**

先写预测，然后打开 [Q1 与更多问题](learning/learning-questions.md#q1)，按 [源码导航](learning/source-navigation.md) 在 IDE 中亲自连接。预测后再查 [完整走读](learning/core-flow.md)。

- [整体职责地图](learning/architecture.md)
- [证据与条件](learning/evidence.md)
- [支线与后续验证](learning/expansion-backlog.md)
- [图谱审计](learning/GRAPH_REPORT.md)
- [模块入口](modules/模块入口.md)
- [主链节点入口](主链节点.md)

这里是导出视图，中文解释的维护来源在 graphify-out/*.md。材料通过静态验收不等于学习者已经掌握。所有测试/行为本轮未运行。
''')
    node_notes={}
    # Graphify note names are unique in graph/; use heading+source to recover IDs.
    candidates={}
    for node in graph['nodes']:
        candidates.setdefault((node.get('label'),node.get('source_file') or ''),[]).append(node['id'])
    for note in sorted((VAULT/'graph').glob('*.md')):
        text=note.read_text(encoding='utf-8')
        src_match=re.search(r'^source_file: (".*")$',text,re.M)
        heading=re.search(r'^# (.*)$',text,re.M)
        if src_match and heading:
            source=json.loads(src_match.group(1))
            ids=candidates.get((heading.group(1),source),[])
            for nid in ids:
                node_notes[nid]=str(note.relative_to(VAULT))
            source_path=Path(source)
            if source and not source_path.is_absolute(): source_path=ROOT/source
            if source and source_path.is_file():
                target=Path(os.path.relpath(source_path,note.parent)).as_posix()
                if '## 源码入口' not in text:
                    put(note,text+'\n\n## 源码入口\n\n['+source+']('+quote(target,safe='/._-')+')\n')
    package_rows=['# 模块入口','','先查看问题，再查解释。包职责详见 [架构地图](../learning/architecture.md)。','']
    for package in provenance['packages']:
        pid='package_'+package['directory'].replace('-','_')
        note=node_notes.get(pid)
        # The library canonicalizes synthetic manifest IDs; match by source/name too.
        if not note:
            for n in graph['nodes']:
                if n.get('label')==package['name'] and n.get('source_file')==package['source_file']:
                    note=node_notes.get(n['id']); break
        body='# '+package['name']+'\n\n'
        body+='预测：这个包拥有主请求的控制、数据、状态，还是只提供边界服务？\n\n'
        body+='[先查源码导航](../learning/source-navigation.md) · [预测后查职责解释](../learning/architecture.md)\n\n'
        if note: body+='[图节点]('+quote('../'+note,safe='/._-')+')\n\n'
        source_rel=Path(os.path.relpath(ROOT/package['source_file'],VAULT/'modules')).as_posix()
        body+='[Manifest]('+quote(source_rel,safe='/._-')+')，直接运行依赖见 provenance.json。\n'
        put(VAULT/'modules'/(package['directory']+'.md'),body)
        package_rows.append('- ['+package['directory']+']('+package['directory']+'.md)')
    put(VAULT/'modules'/'模块入口.md','\n'.join(package_rows))
    overlay=json.loads((OUT/'learning-overlay.json').read_text())
    flow=['# 主链节点导航','','先完成 [Q1/Q2预测](learning/learning-questions.md#q1)，再沿以下节点查源码。[完整解释](learning/core-flow.md)单独链接。','']
    for step in overlay['steps']:
        flow += ['## '+step['label'],'','状态所有者：'+step['state_owner']+'；证据 ['+step['evidence_id']+'](learning/evidence.md#'+step['evidence_id'].lower()+')。','']
        for nid in step['graph_node_ids']:
            if nid in node_notes:
                flow.append('- ['+nid+']('+quote(node_notes[nid],safe='/._-')+')')
        flow.append('')
    put(VAULT/'主链节点.md','\n'.join(flow))
    put(OUT/'obsidian-node-index.json',json.dumps(node_notes,ensure_ascii=False,indent=2))
    put(OUT/'export-manifest.json',json.dumps({'revision':provenance['revision'],'maintenance_sources':names,'derived_learning_pages':generated,'node_index':'obsidian-node-index.json','graphify_notes':len(node_notes),'additional_derived':['obsidian/学习入口.md','obsidian/主链节点.md','obsidian/modules/']},ensure_ascii=False,indent=2))
    print('Exported learning pages and source links:',len(generated),'pages,',len(node_notes),'node mappings')

if __name__=='__main__':
    main()
