"""Static artifact validation only; never imports or runs Pi code/tests."""
import hashlib
import json
import re
import subprocess
import unicodedata
from pathlib import Path
from urllib.parse import unquote

OUT=Path(__file__).resolve().parent
ROOT=OUT.parent
REQUIRED=['PLAN.md','README.md','architecture.md','core-flow.md','source-navigation.md','learning-questions.md','expansion-backlog.md','graph.html','graph.json','GRAPH_REPORT.md','coverage.json','provenance.json','evidence-index.json','question-index.json','learning-overlay.json','extraction.json','rebuild.md','obsidian/学习入口.md','obsidian/主链节点.md','obsidian/modules/模块入口.md']

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(name): return json.loads((OUT/name).read_text())
def slug(s):
    s=re.sub(r'`([^`]*)`',r'\1',s).strip().lower()
    s=''.join(c for c in s if c in '-_' or c.isspace() or unicodedata.category(c)[0] in 'LN')
    return re.sub(r'\s','-',s)
def anchors(path):
    text=path.read_text()
    return {slug(s) for s in re.findall(r'^#{1,6} (.+)$',text,re.M)} | set(re.findall(r'id=["\']([^"\']+)',text))

def main():
    errors=[]
    warnings=[]
    for name in REQUIRED:
        if not (OUT/name).is_file(): errors.append('missing '+name)
    graph=load('graph.json')
    evidence=load('evidence-index.json')
    provenance=load('provenance.json')
    coverage=load('coverage.json')
    ids={n['id'] for n in graph['nodes']}
    if len(ids)!=len(graph['nodes']): errors.append('duplicate graph node IDs')
    if not graph.get('directed'): errors.append('graph must preserve direction')
    for e in graph['links']:
        if e['source'] not in ids or e['target'] not in ids: errors.append('dangling graph link')
    for claim in evidence['claims']:
        path=ROOT/claim['source_file']
        if not path.is_file() or sha(path)!=claim['source_sha256']: errors.append('stale evidence '+claim['id'])
        text=path.read_text()
        for symbol in claim['symbols']:
            if symbol not in text: errors.append('missing symbol '+claim['id']+' '+symbol)
        for nid in claim['graph_node_ids']:
            if nid not in ids: errors.append('missing evidence graph node '+nid)
        if claim['runtime_observed']: errors.append('false runtime evidence '+claim['id'])
    for file in coverage['files']:
        path=ROOT/file['path']
        if sha(path)!=file['sha256']: errors.append('corpus changed '+file['path'])
    if len(coverage['files'])!=coverage['total_detected']: errors.append('corpus count mismatch')
    for question in load('question-index.json')['questions']:
        for entry in question['sources']:
            for nid in entry['graph_node_ids']:
                if nid not in ids: errors.append('missing question graph node '+nid)
    revision=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    status=subprocess.check_output(['git','status','--short'],cwd=ROOT,text=True)
    if revision!=provenance['revision']: errors.append('revision changed')
    if status!=provenance['initial_git_status']+'\n': errors.append('tracked worktree status changed: '+status)
    if sha(OUT/'PLAN.md')!=provenance['plan_sha256']: errors.append('PLAN changed')
    markdown=[OUT/name for name in ('README.md','architecture.md','core-flow.md','source-navigation.md','learning-questions.md','expansion-backlog.md','evidence.md','GRAPH_REPORT.md','rebuild.md')]+list((OUT/'obsidian').rglob('*.md'))
    stems={p.stem for p in (OUT/'obsidian').rglob('*.md')}
    links=0
    wiki_links=0
    anchor_cache={}
    for path in markdown:
        text=path.read_text()
        for label,target in re.findall(r'(?<!!)\[([^\]]*)\]\(([^)]+)\)',text):
            if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',target): continue
            # Ignore code examples that contain placeholder link syntax.
            target=unquote(target.strip('<>'))
            file,sep,anchor=target.partition('#')
            dest=(path.parent/file).resolve() if file else path
            links+=1
            if not dest.is_file():
                errors.append(f'broken link {path.relative_to(OUT)} -> {target}')
            elif sep and dest.suffix=='.md':
                if dest not in anchor_cache: anchor_cache[dest]=anchors(dest)
                if anchor not in anchor_cache[dest]: errors.append(f'broken anchor {path.relative_to(OUT)} -> {target}')
        for target in re.findall(r'\[\[([^\]]+)\]\]',text):
            if path.is_relative_to(OUT/'obsidian'):
                dest=target.split('|')[0].split('#')[0]
                wiki_links+=1
                if dest not in stems and not (path.parent/(dest+'.md')).exists() and not (OUT/'obsidian'/(dest+'.md')).exists():
                    errors.append(f'broken wiki link {path.relative_to(OUT)} -> {target}')
    node_index=load('obsidian-node-index.json')
    for nid,path in node_index.items():
        if nid not in ids or not (OUT/'obsidian'/path).is_file(): errors.append('bad Obsidian node mapping '+nid)
    html=(OUT/'graph.html').read_text()
    if 'vis.DataSet' not in html or 'vis.Network' not in html: errors.append('missing HTML graph initialization')
    if len(load('analysis.json')['communities'])>5000: errors.append('aggregated view exceeds node budget')
    if 'UNKNOWN input/output' not in (OUT/'GRAPH_REPORT.md').read_text(): errors.append('token cost missing honest unknown status')
    h=load('graph-health.json')
    for key in ('dangling_endpoint_edges','self_loop_edges','directed_same_endpoint_collapsed_edges'):
        if h.get(key): warnings.append(f'{key}: {h[key]} (raw extraction; see graph-health.json)')
    warnings.append('215 code files yielded no symbols; packages/tui/test/latex.test.ts partially parsed; long semantic documents use declared overview depths.')
    warnings.append('Browser security policy rejected file:// preview. HTML data/initialization checked statically; browser rendering and interactions not visually verified.')
    result={'status':'pass' if not errors else 'fail','validation_kind':'static artifacts and provenance','revision':revision,'required_files':len(REQUIRED),'graph_nodes':len(ids),'graph_relationships':len(graph['links']),'claims':len(evidence['claims']),'corpus_files_hash_checked':len(coverage['files']),'markdown_links_checked':links,'wiki_links_checked':wiki_links,'obsidian_nodes_mapped':len(node_index),'errors':errors,'warnings':warnings,'runtime_tests_executed':False,'browser_visual_verified':False}
    (OUT/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    printed={**result,'errors':errors[:10],'error_count':len(errors)}
    print(json.dumps(printed,ensure_ascii=False,indent=2))
    if errors: raise SystemExit(1)

if __name__=='__main__': main()
