"""Archive this run's semantic fragments and remove its copied staging sidecars."""
import hashlib
import json
from pathlib import Path

OUT=Path(__file__).resolve().parent
archive=OUT/'semantic-fragments'
archive.mkdir(exist_ok=True)
for source in sorted(OUT.glob('.graphify_chunk_*.json')):
    target=archive/source.name.removeprefix('.graphify_')
    if target.exists():
        if hashlib.sha256(target.read_bytes()).digest()!=hashlib.sha256(source.read_bytes()).digest():
            raise SystemExit('Refusing to overwrite differing fragment '+str(target))
        source.unlink()
    else:
        source.rename(target)
for temporary,retained in [('.graphify_ast.json','structural-extraction.json'),('.graphify_detect.json','corpus.json')]:
    source=OUT/temporary
    if source.exists():
        if json.loads(source.read_text())!=json.loads((OUT/retained).read_text()):
            raise SystemExit('Retained extraction differs: '+temporary)
        source.unlink()
for name in ('.graphify_cached.json','.graphify_uncached.txt','.needs_update'):
    (OUT/name).unlink(missing_ok=True)
coverage=json.loads((OUT/'coverage.json').read_text())
coverage['inventory_zero_symbol_node_files']=sum(f['category']=='code' and f['ast_symbol_node_count']==0 for f in coverage['files'])
coverage['inventory_symbol_count_definition']='Counts non-file-label AST nodes by source. This heuristic count can differ from the extractor 215 zero-symbol warning; per-file values are retained.'
(OUT/'coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
print('Staging cleaned; corpus/AST/semantic extraction and archived fragments retained.')
