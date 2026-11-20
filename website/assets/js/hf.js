/* Prosperity Life School: shared header / footer behaviour (loaded on EVERY page, landing pages included). */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- navigation ---------- */
  var nav = $('#nav'), burger = $('#burger'), body = document.body;
  function place() { var h = nav.closest('.header,.psl-header'); if (h && window.innerWidth <= 900) { nav.style.top = Math.max(0, Math.round(h.getBoundingClientRect().bottom)) + 'px'; } else { nav.style.top = ''; } }
  function setOpen(o) { if (o) place(); nav.classList.toggle('open', o); nav.classList.toggle('psl-open', o); body.classList.toggle('nav-open', o); body.style.overflow = o ? 'hidden' : ''; burger.setAttribute('aria-expanded', o); }
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

  /* ---------- language translate (Google Website Translator) ---------- */
  var sel = $('#langSel');
  function setCookie(v) {
    var host = location.hostname, exp = v ? '' : ';expires=Thu, 01 Jan 1970 00:00:00 UTC';
    var val = v ? '/en/' + v : '';
    document.cookie = 'googtrans=' + val + ';path=/' + exp;
    if (host && host.indexOf('.') > -1) document.cookie = 'googtrans=' + val + ';path=/;domain=.' + host.replace(/^www\./, '') + exp;
  }
  function getCookie() { var m = document.cookie.match(/(?:^|;\s*)googtrans=\/en\/([a-z-]+)/); return m ? m[1] : ''; }
  var gLoaded = false;
  window.googleTranslateElementInit = function () { new google.translate.TranslateElement({ pageLanguage: 'en', includedLanguages: 'kn,gom,hi,ml,ta,te,mr,ar', autoDisplay: false }, 'google_translate_element'); };
  function loadGoogle() { if (gLoaded) return; gLoaded = true; var sc = document.createElement('script'); sc.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit'; sc.onerror = function () { toast('Translation needs an internet connection.'); }; document.head.appendChild(sc); }
  function toast(t) { var d = document.createElement('div'); d.className = 'psl-toast'; d.textContent = t; document.body.appendChild(d); setTimeout(function () { d.remove(); }, 3500); }
  function applyCombo(v, tries) {
    var c = $('.goog-te-combo');
    if (c) { c.value = v; c.dispatchEvent(new Event('change', { bubbles: true })); return; }
    if ((tries || 0) > 50) { toast('Could not load the translator. Please check your internet connection.'); return; }
    setTimeout(function () { applyCombo(v, (tries || 0) + 1); }, 200);
  }
  if (sel) {
    var cur = getCookie();
    try { if (!cur) cur = localStorage.getItem('psl_lang') || ''; } catch (x) { }
    if (cur) { sel.value = cur; loadGoogle(); applyCombo(cur); }
    sel.addEventListener('change', function () {
      var v = sel.value;
      try { localStorage.setItem('psl_lang', v); } catch (x) { }
      setCookie(v);
      if (!v) { var c = $('.goog-te-combo'); if (c) { c.value = ''; c.dispatchEvent(new Event('change', { bubbles: true })); } location.reload(); return; }
      loadGoogle(); applyCombo(v);
    });
  }
})();
