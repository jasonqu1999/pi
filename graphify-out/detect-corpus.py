"""Static scan. All graphify caches and sidecars stay inside graphify-out."""
import json
import os
import sys
from pathlib import Path
from collections import Counter
from graphify.detect import detect

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'graphify-out'
os.chdir(ROOT)
(OUT / '.graphify_python').write_text(sys.executable, encoding='utf-8')
(OUT / '.graphify_root').write_text(str(ROOT), encoding='utf-8')
d = detect(ROOT, cache_root=ROOT, extra_excludes=['graphify-out/', '.codex/'])
(OUT / '.graphify_detect.json').write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({k: v for k, v in d.items() if k != 'files'}, ensure_ascii=False, indent=2))
print('Categories:', {k: len(v) for k,v in d['files'].items()})
print('First-level:', Counter(Path(f).relative_to(ROOT).parts[0] if len(Path(f).relative_to(ROOT).parts)>1 else '(root)' for fl in d['files'].values() for f in fl).most_common(5))
print('Gemini configured:', bool(os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')))
