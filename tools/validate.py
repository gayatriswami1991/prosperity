# -*- coding: utf-8 -*-
"""Sanity checks on site-live/ : SEO tags, schema, links, assets, forms."""
import re, os, sys, json, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = ROOT + '/site-live'
SITE = 'https://www.prosperitylifeschool.com'
bad = 0
def flag(p, m):
    global bad; bad += 1; print('  FAIL', p, m)
pages = sorted(os.path.basename(f) for f in glob.glob(OUT + '/*.html'))
for p in pages:
    s = open('%s/%s' % (OUT, p), encoding='utf8').read()
    noindex = 'noindex' in s
    h1 = re.findall(r'<h1[ >]', s)
    t = re.search(r'<title>(.*?)</title>', s, re.S)
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    can = re.search(r'<link rel="canonical" href="([^"]*)"', s)
    print(p, '| h1:', len(h1), '| title', len(t.group(1)) if t else None, '| desc', len(d.group(1)) if d else None, '| h2:', len(re.findall(r'<h2[ >]', s)),
          '| iframe:', s.count('umang-form"'), '| hf.js' if 'hf.js' in s else '| NO hf.js', '| faq-schema' if '"FAQPage"' in s else '')
    if len(h1) != 1: flag(p, 'H1 count')
    if not t or len(t.group(1)) > 75: flag(p, 'title length')
    if not d or (not noindex and not (70 <= len(d.group(1)) <= 165)): flag(p, 'description length')
    exp = SITE + '/' if p == 'index.html' else SITE + '/' + p
    if not can or can.group(1) != exp: flag(p, 'canonical')
    if not noindex and '<meta name="robots" content="index' not in s: flag(p, 'robots')
    if s.count('<title>') != 1: flag(p, 'multiple titles')
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            j = json.loads(m.group(1)); types = [n.get('@type') for n in j['@graph']]
        except Exception as e: flag(p, 'bad JSON-LD %s' % e)
    # internal links must be absolute www urls
    for m in re.finditer(r'(?:href|action)="([^"]*)"', s):
        h = m.group(1)
        if re.match(r'^(https?:|mailto:|tel:|#|javascript:)', h) or h.startswith("'+") or h.startswith('assets/') or h == '': continue
        flag(p, 'relative link: ' + h)
    for h in re.findall(r'href="(https://www\.prosperitylifeschool\.com[^"#?]*)', s):
        f = h.replace(SITE, '').lstrip('/') or 'index.html'
        if not os.path.exists('%s/%s' % (OUT, f)): flag(p, 'broken internal link ' + h)
    for a in re.findall(r'(?:src|poster|href)="(assets/[^"?#]+)"', s):
        if not os.path.exists('%s/%s' % (OUT, a)): flag(p, 'missing asset ' + a)
    if s.count('href="#"'): flag(p, 'dead href="#" x%d' % s.count('href="#"'))
    if 'alert(' in s: flag(p, 'alert() popup')
    if 'FORM_ENDPOINT' in s or 'psl_leads' in s: flag(p, 'old form code')
    noalt = [i for i in re.findall(r'<img\b[^>]*>', s) if ' alt=' not in i]
    if noalt: flag(p, '%d img without alt' % len(noalt))
    # relative-ness of hash links to existing ids
    ids = set(re.findall(r'\bid="([^"]+)"', s))
    for h in set(re.findall(r'href="#([^"]+)"', s)):
        if h not in ids: flag(p, 'anchor #%s has no target' % h)
for f in ('sitemap.xml', 'robots.txt', 'assets/css/styles.css', 'assets/js/hf.js', 'assets/js/site.js', 'assets/img/og-share.jpg'):
    if not os.path.exists('%s/%s' % (OUT, f)): flag(f, 'missing')
print('ISSUES:', bad)
sys.exit(1 if bad else 0)
