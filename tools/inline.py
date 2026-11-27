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

def split_blocks(css):
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find('{', i)
        if j < 0: break
        head, depth, k = css[i:j].strip(), 1, j + 1
        while depth and k < n:
            depth += (css[k] == '{') - (css[k] == '}'); k += 1
        out.append((head, css[j + 1:k - 1])); i = k
    return out

def split_top(sel):
    parts, depth, cur = [], 0, ''
    for ch in sel:
        if ch in '([': depth += 1
        if ch in ')]': depth -= 1
        if ch == ',' and depth == 0: parts.append(cur); cur = ''
        else: cur += ch
    return parts + [cur]

def shake(css, words):
    """Drop CSS rules whose classes/ids appear nowhere in this page or its scripts, then minify. Keeps file size small for builders."""
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    def keep(blocks):
        res = []
        for head, body in blocks:
            if head.startswith('@media') or head.startswith('@supports'):
                inner = keep(split_blocks(body))
                if inner: res.append(head + '{' + ''.join(inner) + '}')
            elif head.startswith('@keyframes') or head.startswith('@font-face'):
                res.append(('@@' if head.startswith('@keyframes') else '') + head + '{' + re.sub(r'\s+', ' ', body).strip() + '}')
            elif head.startswith('@'): res.append(head + '{' + body + '}')
            else:
                good = [x.strip() for x in split_top(head) if all(c in words for c in re.findall(r'\.([A-Za-z_][\w-]*)', x)) and all(i in words for i in re.findall(r'#([A-Za-z_][\w-]*)', x))]
                if good: res.append(','.join(good) + '{' + re.sub(r'\s*([;:])\s*', r'\1', re.sub(r'\s+', ' ', body)).strip() + '}')
        return res
    out = ''.join(keep(split_blocks(css)))
    # keyframes only if used
    def kf(m):
        name = re.match(r'@@@keyframes\s+([\w-]+)', m.group(0)).group(1)
        return m.group(0)[2:] if re.search(r'animation[^;}]*\b' + re.escape(name) + r'\b', out) else ''
    out = re.sub(r'@@@keyframes[^{]+\{(?:[^{}]|\{[^{}]*\})*\}', kf, out)
    return out

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
    words = set(re.findall(r'[A-Za-z_][\w-]*', s + js['hf'] + js['site']))
    s = s.replace('<link rel="stylesheet" href="assets/css/styles.css">', '<style>' + shake(css, words) + '</style>')
    reels = 'data-reel=' in s
    s = re.sub(r'<script src="assets/js/hf\.js" defer></script>', lambda m: '<script>' + js['hf'] + '</script>', s)
    s = re.sub(r'<script src="assets/js/site\.js" defer></script>', lambda m: (reels_js if reels else '') + '<script>' + js['site'] + '</script>', s)
    s = re.sub(r'\b(src|href|poster)="(assets/[^"]+\.(?:jpg|jpeg|png|gif|svg|webp))"', asset, s)
    left = re.findall(r'(?:src|href|poster)="(assets/[^"]+)"', s)
    name = os.path.basename(f)
    open('%s/%s' % (OUT, name), 'w', encoding='utf8').write(s)
    print(name, round(len(s) / 1048576, 2), 'MB', 'unresolved:', left)
