# -*- coding: utf-8 -*-
"""Make SELF-CONTAINED single-file pages (CSS, JS, photos, reel previews all inside each .html)
for site builders that cannot load an assets/ folder.  Run AFTER tools/build.py.  Output: site-single/"""
import re, os, base64, shutil, glob, mimetypes
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = ROOT + '/site-live', ROOT + '/site-single'
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
def b64(path, mime=None):
    mime = mime or mimetypes.guess_type(path)[0] or 'application/octet-stream'
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(path, 'rb').read()).decode())
css = open(SRC + '/assets/css/styles.css', encoding='utf8').read()
js = {n: open('%s/assets/js/%s.js' % (SRC, n), encoding='utf8').read() for n in ('hf', 'site')}
prev = {n: b64('%s/assets/reels/preview-%d.mp4' % (SRC, n), 'video/mp4') for n in range(1, 7)}
reels_js = '<script>window.PSL_REELS={prev:{%s}};window.PSL_NO_FULL=true;</script>' % ','.join('%d:"%s"' % (n, v) for n, v in prev.items())
cache = {}
def asset(m):
    rel = m.group(2)
    if rel not in cache: cache[rel] = b64('%s/%s' % (SRC, rel))
    return '%s="%s"' % (m.group(1), cache[rel])
for f in sorted(glob.glob(SRC + '/*.html')):
    s = open(f, encoding='utf8').read()
    s = s.replace('<link rel="stylesheet" href="assets/css/styles.css">', '<style>' + css + '</style>')
    reels = 'data-reel=' in s
    s = re.sub(r'<script src="assets/js/hf\.js" defer></script>', lambda m: '<script>' + js['hf'] + '</script>', s)
    s = re.sub(r'<script src="assets/js/site\.js" defer></script>', lambda m: (reels_js if reels else '') + '<script>' + js['site'] + '</script>', s)
    s = re.sub(r'\b(src|href|poster)="(assets/[^"]+\.(?:jpg|jpeg|png|gif|svg|webp))"', asset, s)
    left = re.findall(r'(?:src|href|poster)="(assets/[^"]+)"', s)
    name = os.path.basename(f)
    open('%s/%s' % (OUT, name), 'w', encoding='utf8').write(s)
    print(name, round(len(s) / 1048576, 2), 'MB', 'unresolved:', left)
