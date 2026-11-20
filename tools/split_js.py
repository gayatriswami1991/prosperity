"""One-time helper: split website/assets/js/site.js into hf.js (header/footer behaviour,
used by EVERY page incl. landing pages) and a slimmer site.js (main-site extras)."""
import re
W = '/home/user/prosperity/website/assets/js/'
s = open(W + 'site.js', encoding='utf8').read()

hf = r'''/* Prosperity Life School: shared header / footer behaviour (loaded on EVERY page, landing pages included). */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- navigation ---------- */
  var nav = $('#nav'), burger = $('#burger'), body = document.body;
  function setOpen(o) { nav.classList.toggle('open', o); nav.classList.toggle('psl-open', o); body.classList.toggle('nav-open', o); body.style.overflow = o ? 'hidden' : ''; burger.setAttribute('aria-expanded', o); }
  var isOpen = function (el) { return el.classList.contains('open') || el.classList.contains('psl-open'); };
  var openCls = function (el, on) { el.classList.toggle('open', on); el.classList.toggle('psl-open', on); };
  if (nav && burger) {
    burger.addEventListener('click', function () { setOpen(!isOpen(nav)); });
    $$('li > button', nav).forEach(function (b) {
      b.addEventListener('click', function () {
        var li = b.parentNode, was = isOpen(li);
        $$('li', nav).forEach(function (x) { if (isOpen(x)) { openCls(x, false); var bb = x.querySelector('button'); if (bb) bb.setAttribute('aria-expanded', false); } });
        if (!was) { openCls(li, true); b.setAttribute('aria-expanded', true); }
      });
    });
    $$('a', nav).forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
    document.addEventListener('click', function (e) { if (window.innerWidth > 900 && !e.target.closest('#nav')) $$('li', nav).forEach(function (x) { openCls(x, false); }); });
    window.addEventListener('resize', function () { if (window.innerWidth > 900) setOpen(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
  }

  /* ---------- progress bar + sticky mobile bar (main pages only) ---------- */
  var pg = $('#progress'), stick = $('#stick');
  if (pg || stick) window.addEventListener('scroll', function () {
    var h = document.documentElement;
    if (pg) pg.style.width = (h.scrollTop / Math.max(1, h.scrollHeight - h.clientHeight) * 100) + '%';
    if (stick) stick.classList.toggle('show', window.scrollY > 650);
  }, { passive: true });

'''
i = s.index('  /* ---------- language translate')
tr = s[i:]
hf += tr
open(W + 'hf.js', 'w', encoding='utf8').write(hf)

# ---- slimmer site.js ----
head_end = s.index('(function () {')
cfg = '''/* Prosperity Life School: main-site extras (reveal, counters, home path-finder, SIP, reels, membership links). */
window.PSL_CONFIG = {
  GROUP_URL: '',       // WhatsApp community group invite link (optional)
  WHATSAPP: '918904820166',
  INSTAGRAM: 'https://www.instagram.com/drmariapramila/',
  // Membership links from the client's Google Drive. Paste each URL between the quotes.
  // Empty = the button opens the enquiry form (contact page) instead; empty PDF links stay hidden.
  LINKS: {
    silver_individual: '',  // Silver Individual (website price)
    silver_plus: '',        // Silver Plus
    silver_family: '',      // Silver Family
    gold: '',               // Gold
    onepager_silver: '',    // Silver one-pager PDF
    onepager_gold: '',      // Gold one-pager PDF
    onepager_diamond: '',   // Diamond one-pager PDF
    all_programs_pdf: ''    // PDF with all programs and social links
  }
};

'''
body = s[head_end:i]
# remove navigation block
a = body.index('  /* ---------- navigation')
b = body.index('  /* ---------- scroll reveal')
body = body[:a] + body[b:]
# remove progress/sticky listener
a = body.index("  var pg = $('#progress')")
b = body.index('  /* ---------- count up')
body = body[:a] + body[b:]
# remove confetti + shared lead form + diamond mount, keep data-link handler
a = body.index('  /* ---------- confetti')
b = body.index('  /* membership buttons')
body = body[:a] + body[b:]
# wizard: shared form is now the Umang iframe
body = body.replace("<div class=\"wz-form\" id=\"wzForm\"></div>", "<div class=\"wz-form\" id=\"wzForm\">' + (window.PSL_FORM_HTML || '') + '</div>")
a = body.index("      if (st.step === 2) renderForm(")
b = body.index('\n', a)
body = body[:a] + body[b + 1:]
# reels: lazy source, small preview for cards, full reel for the modal
body = body.replace("""  function reelSrc(n) { return (window.PSL_REELS && window.PSL_REELS[n]) || ('assets/reels/reel-' + n + '.mp4'); }
  $$('video[data-reel]').forEach(function (v) { v.src = reelSrc(v.dataset.reel); });""",
"""  function reelSrc(n) { return 'assets/reels/reel-' + n + '.mp4'; }
  function prevSrc(n) { return 'assets/reels/preview-' + n + '.mp4'; }
  var lazyV = $$('video[data-reel]');
  if ('IntersectionObserver' in window) {
    var lo = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.src = prevSrc(e.target.dataset.reel); lo.unobserve(e.target); } }); }, { rootMargin: '300px' });
    lazyV.forEach(function (v) { lo.observe(v); });
  } else lazyV.forEach(function (v) { v.src = prevSrc(v.dataset.reel); });""")
body = body.replace("closeReel(); } });", "closeReel(); } });")
if 'keydown' not in body:
    body = body.replace("  function openReel", "  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeReel(); });\n  function openReel")
open(W + 'site.js', 'w', encoding='utf8').write(cfg + body.rstrip() + '\n})();\n')
print('ok')
