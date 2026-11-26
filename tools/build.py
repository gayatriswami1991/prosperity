# -*- coding: utf-8 -*-
"""Build the LIVE website into /site-live from:
   website/*-multifile.html   (6 main pages)  +  site-final-landing/*.html (7 ad / booking pages)
Run:  python3 tools/build.py        then zip site-live/ and upload to www.prosperitylifeschool.com
"""
import re, os, sys, json, shutil, hashlib, datetime, subprocess, html as H
sys.path.insert(0, os.path.dirname(__file__))
from seo_data import *

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = ROOT + '/website'
LAND = ROOT + '/site-final-landing'
OUT = ROOT + ('/_blog_demo' if os.environ.get('BLOG_DEMO') else '/site-live')
FORM_URL = 'https://dashboard.umangdigital.co.in/form/contact-form-mtwhdjkv'
WA_CHANNEL = 'https://whatsapp.com/channel/0029Va7vp5iLo4hdA8ZQvC1c'   # public WhatsApp Channel (open to everyone)
SURVEY = 'https://clarity.prosperitylifeschool.com/survey2'            # Financial Clarity Assessment + free 1:1 call
FB_PAGE = 'https://www.facebook.com/drmariacoach/'
GROUP_URL = WA_CHANNEL
WA = 'https://wa.me/918904820166'
SOCIAL = ['https://www.youtube.com/@drmariapramila', 'https://www.youtube.com/@prosperitylifeschool', 'https://www.youtube.com/@SamriddhiwithDrMaria',
          'https://www.instagram.com/drmariapramila/', 'https://www.linkedin.com/in/drmariapramila/', 'https://www.facebook.com/drmariacoach/',
          'https://www.facebook.com/drmariapramila/', WA_CHANNEL]
TODAY = datetime.date.today().isoformat()
NAMES = [p[:-5] for p in PAGE_ORDER] + ['prosperity-thank-you', 'retirement-booking-form']
problems = []


def warn(m): problems.append(m); print('  WARN', m)
def rd(p): return open(p, encoding='utf8').read()
def wr(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w', encoding='utf8').write(s)
def url(page): return SITE + '/' if page == 'index.html' else SITE + '/' + page[:-5]   # clean URLs: no .html
def esc(s): return H.escape(s, quote=True)

# ---------------------------------------------------------------- absolute internal links
LINK_RE = re.compile(r'(["\'])(?:\./)?(' + '|'.join(sorted(NAMES, key=len, reverse=True)) + r')\.html(?=[#?"\'])')
def absolutize(s):
    def rep(m):
        n = m.group(2)
        return m.group(1) + (SITE + '/' if n == 'index' else SITE + '/' + n)
    s = LINK_RE.sub(rep, s)
    return s.replace(SITE + '/#', SITE + '/#')  # no-op, keeps '/#x' valid

# ---------------------------------------------------------------- form
def iframe(extra_id=''):
    return ('<iframe class="umang-form" src="%s" title="Prosperity Life School contact form" width="100%%" height="600" '
            'frameborder="0" style="border:none;" loading="lazy" referrerpolicy="unsafe-url"></iframe>' % FORM_URL)

def form_block(title='Book Your Free Slot', sub='Takes under a minute. Our team will confirm your slot on WhatsApp or by phone.'):
    h = '<div class="form-embed">'
    if title: h += '<h3>%s</h3>' % esc(title)
    if sub: h += '<p class="ph">%s</p>' % esc(sub)
    return h + iframe() + '</div>'

# ---------------------------------------------------------------- schema
def jl(o): return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False, separators=(',', ':')) + '</script>'
ORG_ID, PERSON_ID, WEB_ID = SITE + '/#organization', SITE + '/#drmaria', SITE + '/#website'
ORG = {"@type": ["Organization", "EducationalOrganization", "ProfessionalService"], "@id": ORG_ID, "name": BRAND, "url": SITE + '/',
       "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/logo.png"}, "image": OG_IMAGE,
       "description": "Financial education, financial planning, retirement, protection and income-skills programs for families in India and the Gulf.",
       "email": "maria@prosperitylifeschool.com", "telephone": "+918904820166", "founder": {"@id": PERSON_ID},
       "address": [{"@type": "PostalAddress", "addressLocality": "Bengaluru", "addressRegion": "Karnataka", "addressCountry": "IN"},
                   {"@type": "PostalAddress", "addressLocality": "Mangaluru", "addressRegion": "Karnataka", "addressCountry": "IN"}],
       "areaServed": [{"@type": "City", "name": "Bengaluru"}, {"@type": "City", "name": "Mangaluru"}, {"@type": "Country", "name": "India"}, {"@type": "Place", "name": "Gulf countries"}],
       "contactPoint": [{"@type": "ContactPoint", "telephone": "+918904820166", "email": "maria@prosperitylifeschool.com", "contactType": "customer service", "availableLanguage": ["English", "Kannada", "Tulu", "Konkani"]},
                        {"@type": "ContactPoint", "telephone": "+918073384729", "contactType": "office", "availableLanguage": ["English", "Kannada"]}],
       "sameAs": SOCIAL}
PERSON = {"@type": "Person", "@id": PERSON_ID, "name": "Dr Maria Pramila Dsouza", "jobTitle": "Chartered Wealth Manager and Financial Coach",
          "url": SITE + "/about", "image": SITE + "/assets/img/dr-maria-office.jpg", "worksFor": {"@id": ORG_ID},
          "knowsLanguage": ["English", "Kannada", "Tulu", "Konkani"],
          "knowsAbout": ["Financial planning", "Retirement planning", "Insurance and protection", "Financial literacy", "Wealth creation", "Multiple sources of income"],
          "sameAs": SOCIAL}
WEBSITE = {"@type": "WebSite", "@id": WEB_ID, "url": SITE + "/", "name": BRAND, "inLanguage": "en-IN", "publisher": {"@id": ORG_ID}}

def graph(page, meta, faqs, kind='WebPage', extra=None):
    u = url(page)
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + '/'}]
    if page != 'index.html':
        crumbs.append({"@type": "ListItem", "position": 2, "name": meta['crumb'], "item": u})
    wp = {"@type": kind, "@id": u + '#webpage', "url": u, "name": meta['title'], "description": meta['desc'], "inLanguage": "en-IN",
          "isPartOf": {"@id": WEB_ID}, "about": {"@id": ORG_ID}, "primaryImageOfPage": {"@type": "ImageObject", "url": OG_IMAGE},
          "breadcrumb": {"@id": u + '#breadcrumb'}}
    if extra: wp.update(extra)
    g = [ORG, PERSON, WEBSITE, wp, {"@type": "BreadcrumbList", "@id": u + '#breadcrumb', "itemListElement": crumbs}]
    if faqs:
        g.append({"@type": "FAQPage", "@id": u + '#faq', "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]})
    return {"@context": "https://schema.org", "@graph": g}

def service_node(name, desc, page):
    return {"@type": "Service", "name": name, "serviceType": name, "description": desc, "url": url(page), "provider": {"@id": ORG_ID},
            "areaServed": [{"@type": "Country", "name": "India"}, {"@type": "Place", "name": "Gulf countries"}]}

PROGRAMS = [('Prosperity Clarity Call', 'Free 1-to-1 financial clarity call for families, professionals and NRIs.', 'prosperity-clarity-call-v5.html'),
            ('Retirement Clarity Call', '1-to-1 retirement planning clarity call.', 'prosperity-retirement-clarity-call.html'),
            ('Protection Gap Review', 'Insurance gap analysis and protection review.', 'prosperity-protection-gap-review.html'),
            ('Advisor Career Readiness', 'Career readiness scorecard for aspiring financial advisors.', 'prosperity-advisor-career-readiness.html')]

# ---------------------------------------------------------------- head block
def head_block(page, meta, ld):
    u = url(page)
    robots = 'noindex,follow' if meta.get('noindex') else 'index,follow,max-image-preview:large,max-snippet:-1'
    t, d = esc(meta['title']), esc(meta['desc'])
    return '\n'.join([
        '<title>%s</title>' % t, '<meta name="description" content="%s">' % d, '<meta name="robots" content="%s">' % robots,
        '<link rel="canonical" href="%s">' % u, '<meta name="theme-color" content="#011D43">', '<meta name="author" content="Dr Maria Pramila Dsouza">',
        '<link rel="icon" href="assets/img/logo.png">', '<link rel="apple-touch-icon" href="assets/img/logo.png">',
        '<meta property="og:site_name" content="%s">' % BRAND, '<meta property="og:locale" content="en_IN">', '<meta property="og:type" content="website">',
        '<meta property="og:title" content="%s">' % t, '<meta property="og:description" content="%s">' % d, '<meta property="og:url" content="%s">' % u,
        '<meta property="og:image" content="%s">' % OG_IMAGE, '<meta property="og:image:width" content="1200">', '<meta property="og:image:height" content="630">',
        '<meta property="og:image:alt" content="Dr Maria Pramila Dsouza, Prosperity Life School">',
        '<meta name="twitter:card" content="summary_large_image">', '<meta name="twitter:title" content="%s">' % t,
        '<meta name="twitter:description" content="%s">' % d, '<meta name="twitter:image" content="%s">' % OG_IMAGE,
        jl(ld)])

STRIP_HEAD = [r'<title>.*?</title>', r'<meta\s+name="description"[^>]*>', r'<meta\s+property="og:[^>]*>', r'<meta\s+name="twitter:[^>]*>',
              r'<meta\s+name="robots"[^>]*>', r'<link\s+rel="canonical"[^>]*>', r'<link\s+rel="icon"[^>]*>',
              r'<script\s+type="application/ld\+json">.*?</script>']
def set_head(s, page, meta, ld, extra_head=''):
    head_end = s.index('</head>')
    head, rest = s[:head_end], s[head_end:]
    for p in STRIP_HEAD:
        head = re.sub(p, '', head, flags=re.S | re.I)
    head = re.sub(r'\n\s*\n+', '\n', head)
    return head + head_block(page, meta, ld) + '\n' + extra_head + rest

# ---------------------------------------------------------------- FAQ
def faq_section(title, faqs):
    det = ''.join('<details><summary>%s</summary><p>%s</p></details>' % (esc(q), esc(a)) for q, a in faqs)
    return ('<section class="bg-cream reveal" id="faq"><div class="wrap"><div class="sec-head"><span class="eyebrow">FAQ</span><h2>%s</h2></div>'
            '<div class="faqs">%s</div></div></section>\n' % (esc(title), det))

def parse_details(s):
    return [(H.unescape(re.sub('<[^>]+>', '', q)).strip(), H.unescape(re.sub('<[^>]+>', '', a)).strip())
            for q, a in re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>', s, re.S)]


# ---------------------------------------------------------------- blog
def load_posts():
    posts = json.load(open(os.path.dirname(__file__) + '/blogs.json', encoding='utf8'))
    if os.environ.get('BLOG_DEMO'):   # preview only (never shipped): sample cards to review the design
        posts = [{"title": "Sample article title goes here", "image": "assets/img/dr-maria-office.jpg", "date": "2026-11-18",
                  "intro": "A short two-line introduction that tells the reader what this article will help them understand.", "url": SITE + "/blog"}] * 5
    return sorted(posts, key=lambda p: p['date'], reverse=True)

def fmt_date(d): return datetime.date.fromisoformat(d).strftime('%d %b %Y').lstrip('0')

def blog_cards(posts, limit=None):
    posts = posts[:limit] if limit else posts
    if not posts:
        return ('<div class="bempty"><h3>Our first articles are on the way</h3><p>Plain-language money insights from Dr Maria are coming soon. '
                'Meanwhile, you can watch free videos and reels.</p><a class="btn" href="youtube.html">Watch Free Videos</a></div>')
    out = ''
    for p in posts:
        u, t = esc(p['url']), esc(p['title'])
        out += ('<article class="bcard"><a class="bimg" href="%s" target="_blank" rel="noopener"><img src="%s" alt="%s" loading="lazy" width="1200" height="675"></a>'
                '<div class="bb"><time datetime="%s">%s</time><h3><a href="%s" target="_blank" rel="noopener">%s</a></h3><p>%s</p>'
                '<a class="more" href="%s" target="_blank" rel="noopener">Read the article <svg class="ic"><use href="#i-arrow"/></svg></a></div></article>'
                % (u, esc(p['image']), t, p['date'], fmt_date(p['date']), u, t, esc(p['intro']), u))
    return '<div class="bgrid">%s</div>' % out

def blog_main(posts):
    return ('<main>\n<section class="phero" id="top"><div class="floaties" aria-hidden="true"><span class="fl f1">\u20b9</span><span class="fl f3">\u2726</span></div>\n'
            '<div class="wrap" style="position:relative;z-index:1;text-align:center;max-width:860px"><span class="pill">Blog</span>'
            '<h1>Money, Insurance and <em>Retirement Insights</em></h1>'
            '<p class="lede" style="margin-left:auto;margin-right:auto">Short, plain-language articles from Dr Maria Pramila Dsouza to help your family make clearer money decisions.</p></div></section>\n'
            '<section class="reveal" id="posts" style="padding-top:60px"><div class="wrap">\n<!-- BLOG POSTS: generated from tools/blogs.json. One card = <article class="bcard">...</article> -->\n'
            + blog_cards(posts) + '\n<p class="fine" style="color:var(--ink-soft);text-align:center">Educational content, not investment advice.</p></div></section>\n'
            '<section class="bg-mist reveal" id="start"><div class="wrap" style="text-align:center;max-width:760px"><h2>Prefer to Talk It Through?</h2>'
            '<p class="muted" style="margin-top:12px">Book a free 1-to-1 conversation and bring your questions.</p>'
            '<div class="cta-row center" style="margin-top:22px"><a class="btn lg" href="contact.html">Book a Free Call</a><a class="btn navy lg" href="community.html">Join the Community</a></div></div></section>\n</main>')

def home_blog_section(posts):
    return ('<section class="bg-cream reveal" id="blog"><div class="wrap"><div class="sec-head"><span class="eyebrow">From the blog</span>'
            '<h2>Latest Money Insights</h2><p>Plain-language articles on insurance, retirement, SIPs and family money.</p></div>\n'
            + blog_cards(posts, 3) + '\n<div class="cta-row center" style="margin-top:30px"><a class="btn navy lg" href="blog.html">View All Articles</a></div></div></section>\n')

FB_SYMBOL = '<symbol id="b-fb" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></symbol>'
def global_patches(s, page):
    # client number: 1,000+ client families
    s = s.replace('data-count="500" data-suf="+">500+</b>', 'data-count="1000" data-suf="+">1,000+</b>')
    s = re.sub(r'500\+(</b>\s*(?:<span>)?\s*[Cc]lient famil)', r'1,000+\1', s)
    s = re.sub(r'500\+( client famil)', r'1,000+\1', s)
    # Facebook icon (page link from client) next to YouTube in every social row + sprite symbol
    s = re.sub(r'(<a class="s-yt"[^>]*>.*?</a>)', lambda m: m.group(1) + '<a class="s-fb" href="%s" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24"><use href="#b-fb"/></svg></a>' % FB_PAGE, s, flags=re.S)
    if 'id="b-fb"' not in s: s = s.replace('</defs>', FB_SYMBOL + '</defs>', 1)
    # header / menu / sticky "Free Assessment" -> the client's real assessment
    s = re.sub(r'<a class="btn( sm)?" href="prosperity-clarity-call-v5\.html">((?:Take )?Free Assessment)</a>',
               lambda m: '<a class="btn%s" href="%s" target="_blank" rel="noopener">%s</a>' % (m.group(1) or '', SURVEY, m.group(2)), s)
    s = s.replace('<a class="btn lg" href="prosperity-clarity-call-v5.html">Get Your Free Clarity Assessment', '<a class="btn lg" href="%s" target="_blank" rel="noopener">Get Your Free Clarity Assessment' % SURVEY)
    # footer: office phone + WhatsApp channel
    foot = '<li><svg><use href="#i-pin"/></svg><span>Bengaluru &amp; Mangaluru'
    if foot in s:
        s = s.replace(foot, '<li><svg><use href="#i-phone"/></svg><a href="tel:+918073384729">Office +91 80733 84729</a></li>\n<li><svg><use href="#i-chat"/></svg><a href="%s" target="_blank" rel="noopener">WhatsApp Channel</a></li>\n' % WA_CHANNEL + foot, 1)
    else: warn(page + ': footer contact anchor missing')
    return s

# ---------------------------------------------------------------- main pages
def build_main():
    posts = load_posts()
    sprite = hdr = ftr = None
    for page in [p for p in PAGE_ORDER if p in MAIN]:
        meta = MAIN[page]
        s = rd('%s/%s-multifile.html' % (W, 'contact' if page == 'blog.html' else page[:-5]))
        if page == 'blog.html':
            s = re.sub(r'<main>.*?</main>', lambda m: blog_main(posts), s, flags=re.S)
        s = global_patches(s, page)
        NAVY = '<li><a href="youtube.html">YouTube</a></li>'
        if s.count(NAVY) != 2: warn(page + ': nav anchor count %d' % s.count(NAVY))
        s = s.replace(NAVY, NAVY + '<li><a href="blog.html">Blog</a></li>')
        if page == 'index.html':
            s = s.replace('<section class="bg-mist reveal" id="stories">', home_blog_section(posts) + '<section class="bg-mist reveal" id="stories">', 1)
        if page == 'index.html':
            sprite = re.search(r'<!-- icon sprite -->\s*(<svg width="0".*?</svg>)', s, re.S).group(1)
            hdr = re.search(r'<div class="topbar">.*?</header>', s, re.S).group(0)
            ftr = re.search(r'<footer class="footer">.*?</footer>', s, re.S).group(0)
        # H1 keyword line
        m = re.search(r'<h1([^>]*)>', s)
        s = s[:m.end()] + '<span class="h1kw">%s</span>' % meta['kw'] + s[m.end():]
        # H2 changes
        for old, new in meta['h2']:
            if old in s: s = s.replace(old, new, 1)
            else: warn('%s: H2 not found: %s' % (page, old))
        # forms
        def mount(m):
            a = m.group(0)
            g = lambda k: (re.search(k + '="([^"]*)"', a) or [None, ''])[1]
            return form_block(g('data-title') if 'data-kind' not in a else '', g('data-sub') if 'data-kind' not in a else '')
        s = re.sub(r'<div class="pform-mount[^"]*"[^>]*></div>', mount, s)
        if 'pform-mount' in s: warn(page + ': leftover form mount')
        # FAQ
        faqs = meta['faq']
        if faqs:
            block = faq_section(meta['faq_title'], faqs)
            m = re.search(r'<section[^>]*id="start"', s) or re.search(r'<section[^>]*id="legal"', s)
            if not m: warn(page + ': no FAQ anchor');
            else: s = s[:m.start()] + block + s[m.start():]
        else:
            faqs = parse_details(s)
        # extra SEO line on community h2 faq heading
        s = s.replace('<h2>Before You Join</h2>', '<h2>Joining a Financial Literacy Community in India: Before You Join</h2>')
        # wizard template (home)
        if page == 'index.html':
            s = s.replace('</body>', '<template id="pslFormTpl">' + form_block('Book My Free Slot', 'Leave your details and we will confirm your slot. Takes under a minute.') + '</template>\n</body>')
        # scripts
        s = s.replace('<script src="assets/js/site.js" defer></script>', '<script src="assets/js/hf.js" defer></script>\n<script src="assets/js/site.js" defer></script>')
        s = s.replace('<a class="pdf" href="#" data-link=', '<a class="pdf" href="%s/programs#memberships" hidden data-link=' % SITE)
        # schema
        kind, extra = 'WebPage', None
        if meta['schema'] == 'about': kind, extra = 'AboutPage', {"mainEntity": {"@id": PERSON_ID}}
        elif meta['schema'] == 'contact': kind = 'ContactPage'
        elif meta['schema'] in ('programs', 'youtube'): kind = 'CollectionPage'
        elif meta['schema'] == 'blog':
            kind = 'Blog'
            extra = {"blogPost": [{"@type": "BlogPosting", "headline": p['title'], "image": p['image'] if p['image'].startswith('http') else SITE + '/' + p['image'],
                                   "datePublished": p['date'], "url": p['url'], "description": p['intro'], "author": {"@id": PERSON_ID}, "publisher": {"@id": ORG_ID}} for p in load_posts()]}
        if meta['schema'] == 'programs':
            extra = {"mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": service_node(*p)} for i, p in enumerate(PROGRAMS)]}}
        if meta['schema'] == 'youtube':
            extra = {"about": {"@type": "Thing", "name": "Dr Maria's Finance Chapel", "url": SOCIAL[0]}}
        ld = graph(page, meta, faqs, kind, extra)
        s = set_head(s, page, meta, ld)
        s = absolutize(s)
        if s.count('<h1') != 1: warn('%s: H1 count %d' % (page, s.count('<h1')))
        wr('%s/%s' % (OUT, page), s)
        print('main', page, len(s) // 1024, 'KB')
    return sprite, hdr, ftr

# ---------------------------------------------------------------- scoped header/footer for landing pages
NO_RENAME = {'notranslate', 'skiptranslate', 'nav-open'}
def prefix_classes(markup):
    def rep(m):
        return 'class="%s"' % ' '.join(c if c in NO_RENAME else 'psl-' + c for c in m.group(1).split())
    return re.sub(r'class="([^"]*)"', rep, markup)

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

def scoped_css(css, markup):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    root = dict(re.findall(r'(--[\w-]+)\s*:\s*([^;]+);', re.search(r':root\s*\{(.*?)\}', css, re.S).group(1)))
    hf = set(c for g in re.findall(r'class="([^"]*)"', markup) for c in g.split())
    allowed = hf | {'open', 'show', 'sr', 'on'}
    ids = {'nav', 'burger', 'langSel', 'stick', 'progress', 'google_translate_element'}
    kf, used = {}, []
    def ren(s): return re.sub(r'\.([A-Za-z_][\w-]*)', lambda m: '.' + (m.group(1) if m.group(1) in NO_RENAME else 'psl-' + m.group(1)), s)
    def keep(blocks):
        res = []
        for head, body in blocks:
            if head.startswith('@media') or head.startswith('@supports'):
                inner = keep(split_blocks(body))
                if inner: res.append(head + '{' + ''.join(inner) + '}')
            elif head.startswith('@keyframes'): kf[head.split()[1]] = (head, body)
            elif head.startswith('@') or head.startswith(':root'): continue
            else:
                good = []
                for sel in [x.strip() for x in head.split(',')]:
                    cls = re.findall(r'\.([A-Za-z_][\w-]*)', sel); idl = re.findall(r'#([\w-]+)', sel)
                    if (cls or idl) and all(c in allowed for c in cls) and all(i in ids for i in idl) and ((set(cls) & hf) or idl) and not re.search(r'\b(html|body)\b', sel.replace('body.nav-open', '')):
                        good.append(ren(sel))
                if good: res.append(','.join(good) + '{' + body + '}')
        return res
    out = ''.join(keep(split_blocks(css)))
    for _ in range(3): out = re.sub(r'var\((--[\w-]+)\)', lambda m: root.get(m.group(1), 'inherit').strip(), out)
    for name, (head, body) in kf.items():
        if name in out: out += head + '{' + body + '}'
    def each(tmpl):   # plain selectors only (no :where/:is), for strict builders
        return ','.join(tmpl % r for r in ('.psl-topbar', '.psl-header', '.psl-footer'))
    base = (".psl-topbar,.psl-header,.psl-footer,.psl-wa,.psl-stick{font-family:'Poppins',Arial,sans-serif;font-size:16px;line-height:1.65;color:#0F2342;text-align:left;-webkit-font-smoothing:antialiased}"
            + each('%s *') + "{box-sizing:border-box}"
            + each('%s a') + "{text-decoration:none}"
            + ".psl-topbar ul,.psl-header ul:not(.psl-nav),.psl-footer ul{margin:0;padding:0;list-style:none}"
            + each('%s p') + ',' + each('%s h4') + ',' + each('%s li') + "{margin:0}"
            + ".psl-header img,.psl-footer img{max-width:100%;display:block;height:auto}"
            + each('%s select') + ',' + each('%s button') + "{font-family:inherit}"
            + each('%s p') + ',' + each('%s li') + ',' + each('%s span') + ',' + each('%s div') + ',' + each('%s h4') + "{color:inherit}"
            ".psl-header .psl-sub a{display:block}"
            "body{top:0!important}.skiptranslate iframe,.goog-te-banner-frame,#goog-gt-tt,.goog-te-balloon-frame{display:none!important}.goog-text-highlight{background:none!important;box-shadow:none!important}"
            ".psl-gt-hide,#google_translate_element{display:none}"
            ".psl-toast{position:fixed;left:50%;bottom:90px;transform:translateX(-50%);background:#011D43;color:#fff;padding:12px 20px;border-radius:50px;font-size:14px;z-index:900}")
    return base + out

LP_CSS = """
.form-embed{background:#fff;border-radius:18px;padding:22px 18px 14px;box-shadow:0 20px 44px -24px rgba(0,0,0,.45);margin:22px 0;min-width:0;color:#0F2342;font-family:'Manrope',Arial,sans-serif}
.form-embed h3{margin:0 0 4px;font-size:22px;color:#011D43;line-height:1.2;font-family:inherit}
.form-embed .ph{margin:0 0 12px;color:#4B5B75;font-size:14.5px;line-height:1.5}
.umang-form{display:block;width:100%;height:600px;border:0}
@media(max-width:560px){.umang-form{height:700px}.form-embed{padding:16px 10px 10px}}
.lp-disc{background:#001330;color:rgba(255,255,255,.62);font:400 12.5px/1.75 'Poppins',Arial,sans-serif}
.lp-disc-in{max-width:1200px;margin:0 auto;padding:22px 28px 0}
.lp-disc b{color:#E8BC5A}
.faq-q{text-align:left}
.lp-alt{margin:0 0 18px;font-size:14px;color:rgba(255,255,255,.85)}.lp-alt a{color:#E8BC5A;text-decoration:underline;font-weight:700}
"""

def landing_head_extra(css):
    return ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">'
            '<style id="psl-hf">%s%s</style>' % (css, LP_CSS))

# ---------------------------------------------------------------- landing pages
IMG_RE = re.compile(r'data:image/(png|jpeg|jpg|webp|gif|svg\+xml);base64,([A-Za-z0-9+/=]+)')
def extract_images(s, page):
    seen = {}
    def rep(m):
        ext = {'jpeg': 'jpg', 'svg+xml': 'svg'}.get(m.group(1), m.group(1))
        import base64
        data = base64.b64decode(m.group(2))
        h = hashlib.md5(data).hexdigest()[:10]
        rel = 'assets/lp/%s.%s' % (h, ext)
        p = '%s/%s' % (OUT, rel)
        if rel not in seen:
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, 'wb').write(data); seen[rel] = len(data)
            if ext in ('jpg', 'png') and len(data) > 250 * 1024:
                try:
                    from PIL import Image
                    im = Image.open(p)
                    if im.width > 1400: im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
                    if ext == 'jpg': im.convert('RGB').save(p, quality=82, optimize=True, progressive=True)
                    else: im.save(p, optimize=True)
                except Exception as e: warn('image optimise failed %s' % e)
        return rel
    return IMG_RE.sub(rep, s)

def add_lazy_dims(s):
    from PIL import Image
    first = [True]
    def rep(m):
        tag = m.group(0)
        if 'width=' in tag or 'height=' in tag: return tag
        src = re.search(r'src="(assets/lp/[^"]+)"', tag)
        if not src or src.group(1).endswith('.svg'): return tag
        try:
            w, h = Image.open('%s/%s' % (OUT, src.group(1))).size
        except Exception: return tag
        add = ' width="%d" height="%d"' % (w, h)
        if first[0]: first[0] = False
        else: add += ' loading="lazy" decoding="async"'
        if tag.endswith('/>'): return tag[:-2].rstrip() + add + '/>'
        return tag[:-1] + add + '>'
    return re.sub(r'<img\b[^>]*>', rep, s)

def faq_item(style, q, a):
    if style == 'span':
        return '<div class="faq-item"><button class="faq-q"><span>%s</span><span class="icon">+</span></button><div class="faq-a"><div class="faq-a-inner">%s</div></div></div>' % (esc(q), esc(a))
    return '<div class="faq-item"><button class="faq-q" type="button">%s<span class="icon">+</span></button><div class="faq-a"><div class="faq-a-inner">%s</div></div></div>' % (esc(q), esc(a))

def parse_faq_items(s):
    out = []
    pats = [r'<div class="faq-item">\s*<button class="faq-q"[^>]*>(.*?)<span class="icon">\+</span></button>\s*<div class="faq-a"><div class="faq-a-inner">(.*?)</div></div>\s*</div>',
            r'<div class="fi"><button class="fq"[^>]*>(.*?)<span class="icon">\+</span></button><div class="fa"><div>(.*?)</div></div></div>']
    for pat in pats:
        for m in re.finditer(pat, s, re.S):
            out.append((H.unescape(re.sub('<[^>]+>', '', m.group(1))).strip(), H.unescape(re.sub('<[^>]+>', '', m.group(2))).strip()))
    return out

def build_landing(sprite, hdr, ftr):
    markup = hdr + ftr
    css = scoped_css(rd(W + '/assets/css/styles.css') + rd(os.path.dirname(__file__) + '/extra.css'), markup)
    head_html = prefix_classes(hdr).replace('<header class="psl-header">', '<div class="psl-header" role="banner">').replace('</header>', '</div>')
    head_html = prefix_classes(hdr)
    head_html = head_html.replace('<header class="psl-header">', '<div class="psl-header" role="banner">').replace('</header>', '</div>')
    foot_html = prefix_classes(ftr).replace('<footer class="psl-footer">', '<div class="psl-footer" role="contentinfo">').replace('</footer>', '</div>')
    for page, meta in LANDING.items():
        s = rd('%s/%s' % (LAND, page))
        s = extract_images(s, page)
        # --- placeholders / popups
        s = re.sub(r'<a ([^>]*?)href="#"([^>]*?)onclick="alert\([^"]*\); return false;"', r'<a \1href="youtube.html"\2', s)
        s = re.sub(r'<a ([^>]*?)onclick="alert\([^"]*\); return false;"([^>]*?)href="#"', r'<a \1\2href="youtube.html"', s)
        # --- old nav + footer
        s = re.sub(r'<nav class="nav">.*?</nav>', '', s, flags=re.S)
        disc = ''
        fm = re.search(r'<footer[^>]*>(.*?)</footer>', s, re.S)
        if fm:
            inner = re.sub(r'<div class="links">.*?</div>', '', fm.group(1), flags=re.S)
            inner = re.sub(r'</div>\s*<div[^>]*>', ' \u00b7 ', inner.strip())
            inner = re.sub(r'<div class="wrap">', '', inner)
            inner = re.sub(r'<(/?)(div|p)[^>]*>', ' ', inner)
            inner = re.sub(r'<br\s*/?>', ' ', inner); inner = re.sub(r'\s+', ' ', inner).strip()
            disc = '<div class="lp-disc"><div class="lp-disc-in">%s</div></div>' % inner
            s = s[:fm.start()] + disc + foot_html + s[fm.end():]
        else: warn(page + ': no footer')
        # --- site header after <body>
        s = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + '\n' + sprite + '\n' + head_html + '\n', s, count=1)
        # --- forms per page
        fb = form_block('Book Your Free Call', 'Takes under a minute. Our team will confirm your slot on WhatsApp or by phone.')
        if page == 'prosperity-clarity-call-v5.html':
            s, n = re.subn(r'<div class="cta-row">\s*<a href="#" class="btn btn-pulse">Apply for My Free Clarity Call</a>\s*</div>', fb, s)
        elif page == 'prosperity-protection-gap-review.html':
            alt = '<p class="lp-alt">Prefer a quick self-check first? <a href="https://links.prosperitylifeschool.com/insurance-assessment" target="_blank" rel="noopener">Insurance Assessment</a> &middot; <a href="https://links.prosperitylifeschool.com/pls-accins-assessment" target="_blank" rel="noopener">Accidental Insurance Assessment</a></p>'
            s, n = re.subn(r'<div class="cta-row">\s*<a class="btn btn-pulse" href="#">Book My Complimentary Protection Clarity Call</a>\s*</div>', lambda m: fb + alt, s)
        elif page == 'prosperity-advisor-career-readiness.html':
            s = s.replace('href="contact.html"', 'href="#apply"')
            s, n = re.subn(r'<a class="btn big js-book" href="#apply">Start: It Takes About a Minute <span class="arr">→</span></a>', fb, s)
        elif page == 'prosperity-retirement-clarity-call.html':
            i = s.index('id="book"')
            m = re.compile(r'<div class="cta-row"><a class="btn big btn-pulse" href="book-retirement-clarity-call.html">.*?</a></div>', re.S).search(s, i)
            n = 1 if m else 0
            if m: s = s[:m.start()] + fb + s[m.end():]
            s = s.replace('<a class="btn big btn-pulse" href="book-retirement-clarity-call.html">Book My 1-to-1 Prosperity Retirement Clarity Call <span class="arr">→</span></a>', '<a class="btn big btn-pulse" href="#book">Book My 1-to-1 Prosperity Retirement Clarity Call <span class="arr">→</span></a>')
        elif page == 'retirement-booking-form.html':
            a = s.index('<div class="card" id="card">'); b = s.index('<aside class="side">')
            s = s[:a] + '<div class="card" id="card"><div class="c-body">' + iframe() + '</div></div>\n' + s[b:]
            s = re.sub(r'<script>.*?</script>', '', s, flags=re.S); n = 1
        elif page == 'prosperity-thank-you.html':
            s = s.replace('<h2>Join Our VIP WhatsApp Community</h2>', '<h2>Join Our WhatsApp Channel</h2>')
            s = s.replace('Get exclusive financial-clarity tips, event updates and first access to future Prosperity Life School sessions.', 'Get daily money content and updates from Dr Maria. The channel is open to everyone.')
            s = s.replace('href="#" class="btn btn-pulse">Join VIP WhatsApp Community', 'href="%s" class="btn btn-pulse" target="_blank" rel="noopener">Join the WhatsApp Channel' % WA_CHANNEL); n = 1
        else: n = 1
        if not n: warn(page + ': form not placed')
        # --- kicker + H2s + FAQs
        if meta.get('kicker'):
            if meta['kicker'][0] in s: s = s.replace(meta['kicker'][0], meta['kicker'][1], 1)
            else: warn(page + ': kicker not found')
        for old, new in meta['h2']:
            if old in s: s = s.replace(old, new, 1)
            else: warn('%s: H2 not found: %s' % (page, old))
        faqs = None
        if meta.get('faq'):
            style = 'span' if re.search(r'class="faq-q"><span>', s) else 'plain'
            new_items = ''.join(faq_item(style, q, a) for q, a in meta['faq'])
            m = re.search(r'(<div class="faq(?:-list)?">)', s)
            if m: s = s[:m.end()] + new_items + s[m.end():]
            else: warn(page + ': faq container not found')
        if page != 'prosperity-thank-you.html' and ('faq-item' in s or 'class="fi"' in s):
            faqs = parse_faq_items(s)
            if not faqs: warn(page + ': could not parse faq items')
        # --- links, scripts, lazy images
        s = re.sub(r'500\+(</b>\s*(?:<span>)?\s*[Cc]lient famil)', r'1,000+\1', s)
        s = re.sub(r'500\+( client famil)', r'1,000+\1', s)
        s = absolutize(s)
        s = s.replace('</body>', '<script src="assets/js/hf.js" defer></script>\n</body>')
        # --- schema + head
        extra = {}
        ld = graph(page, meta, faqs, 'WebPage')
        if meta.get('service'):
            ld['@graph'].append(dict(service_node(meta['service'], meta['desc'], page), **{"@id": url(page) + '#service'}))
        s = set_head(s, page, meta, ld, landing_head_extra(css))
        s = add_lazy_dims(s)
        if s.count('<h1') != 1: warn('%s: H1 count %d' % (page, s.count('<h1')))
        wr('%s/%s' % (OUT, page), s)
        print('landing', page, len(s) // 1024, 'KB', 'faqs', len(faqs or []))

# ---------------------------------------------------------------- assets + extras
def build_assets():
    A = OUT + '/assets'
    if os.path.exists(A): shutil.rmtree(A)
    shutil.copytree(W + '/assets', A, ignore=shutil.ignore_patterns('main.js', 'small-*.mp4'))
    css = rd(W + '/assets/css/styles.css') + rd(os.path.dirname(__file__) + '/extra.css')
    wr(A + '/css/styles.css', css)
    for n in ('hf', 'site'): wr(A + '/js/%s.js' % n, absolutize(rd(W + '/assets/js/%s.js' % n)))
    # share image 1200x630
    try:
        subprocess.run(['convert', '-size', '1200x630', 'gradient:#011D43-#001330', W + '/assets/img/dr-maria-office.jpg', '-resize', 'x630', '-gravity', 'east', '-composite',
                        W + '/assets/img/logo-transparent.png', '-resize', '150x150', '-gravity', 'northwest', '-geometry', '+60+60', '-composite',
                        '-fill', 'white', '-font', 'DejaVu-Sans-Bold', '-pointsize', '54', '-gravity', 'west', '-annotate', '+60-30', 'Prosperity Life School',
                        '-fill', '#E8BC5A', '-font', 'DejaVu-Sans', '-pointsize', '28', '-annotate', '+60+50', 'Financial planning and education',
                        '-quality', '86', A + '/img/og-share.jpg'], check=True, capture_output=True)
    except Exception as e: warn('og image failed: %s' % e)

def build_extras():
    pages = [p for p in PAGE_ORDER]
    pri = {'index.html': '1.0', 'contact.html': '0.8', 'programs.html': '0.9'}
    urls = ''.join('  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>\n' % (
        url(p), TODAY, 'weekly' if p in ('index.html', 'youtube.html') else 'monthly', pri.get(p, '0.8' if p.startswith('prosperity') else '0.7')) for p in pages)
    wr(OUT + '/sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
    wr(OUT + '/robots.txt', 'User-agent: *\nAllow: /\nDisallow: /prosperity-thank-you\nDisallow: /retirement-booking-form\n\nSitemap: %s/sitemap.xml\n' % SITE)
    wr(OUT + '/README.txt', """Prosperity Life School: LIVE website (www.prosperitylifeschool.com)

UPLOAD: put ALL files and the assets/ folder (and .htaccess, which is hidden) in the root of the website (public_html).
Pages (13): index, about, programs, community, youtube, contact + 4 ad landing pages + book-retirement-clarity-call,
retirement-booking-form, prosperity-thank-you. Extra: sitemap.xml, robots.txt, .htaccess (https + www redirect, clean URLs without .html, cache).

FORM: every page uses the same Umang Digital form (iframe). To change it, edit FORM_URL in tools/build.py and rebuild.
LINKS: membership / PDF links live in assets/js/site.js (PSL_CONFIG.LINKS). Empty = button goes to the Contact page.
AFTER GO-LIVE: submit https://www.prosperitylifeschool.com/sitemap.xml in Google Search Console.
Rebuild:  python3 tools/build.py  then  python3 tools/validate.py
""")

    wr(OUT + '/.htaccess', """# Apache / cPanel: force https + www, hide index.html, compress and cache
RewriteEngine On
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} !^www\\. [NC]
RewriteRule ^(.*)$ https://www.prosperitylifeschool.com/$1 [L,R=301]
RewriteCond %{THE_REQUEST} \\s/index\\.html[\\s?] [NC]
RewriteRule ^index\\.html$ / [L,R=301]
RewriteCond %{THE_REQUEST} \\s/+([^\\s?]+)\\.html[\\s?] [NC]
RewriteRule ^ /%1 [L,R=301]
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^([^./]+)$ $1.html [L]
<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml
</IfModule>
<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType image/jpeg "access plus 1 year"
ExpiresByType image/png "access plus 1 year"
ExpiresByType video/mp4 "access plus 1 year"
ExpiresByType text/css "access plus 1 month"
ExpiresByType application/javascript "access plus 1 month"
ExpiresByType text/html "access plus 0 seconds"
</IfModule>
""")

if __name__ == '__main__':
    if os.path.exists(OUT):
        for f in os.listdir(OUT):
            p = os.path.join(OUT, f)
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    os.makedirs(OUT, exist_ok=True)
    build_assets()
    sprite, hdr, ftr = build_main()
    build_landing(sprite, hdr, ftr)
    build_extras()
    print('DONE, warnings:', len(problems))
    for p in problems: print(' -', p)
