import json
import os
from pathlib import Path
from graphify.extract import extract
from graphify.cache import check_semantic_cache

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'graphify-out'
os.chdir(ROOT)
d = json.loads((OUT / '.graphify_detect.json').read_text())
spec = '/Users/jason/.codex/skills/graphify/references/extraction-spec.md'
files = [f for cat in ('document','paper','image') for f in d['files'][cat]]
n,e,h,u = check_semantic_cache(files, root=ROOT, prompt_file=spec)
(OUT / '.graphify_cached.json').write_text(json.dumps({'nodes':n,'edges':e,'hyperedges':h}), encoding='utf-8')
(OUT / '.graphify_uncached.txt').write_text('\n'.join(u), encoding='utf-8')
# Keep directory neighbours together. Images are always individual chunks.
docs = [f for f in u if f not in d['files']['image']]
chunks = [docs[i:i+22] for i in range(0,len(docs),22)] + [[f] for f in u if f in d['files']['image']]
(OUT / 'semantic-batches.json').write_text(json.dumps(chunks,indent=2),encoding='utf-8')
print(f'Cache hits {len(files)-len(u)}; uncached {len(u)}; chunks {len(chunks)}', flush=True)
result = extract([Path(f) for f in d['files']['code']], cache_root=ROOT, root=ROOT, parallel=False)
(OUT / '.graphify_ast.json').write_text(json.dumps(result,ensure_ascii=False),encoding='utf-8')
print(f'AST: {len(result["nodes"])} nodes; {len(result["edges"])} edges',flush=True)
