/* Prosperity Life School: one shared script for every main page. */

/* ================= SETTINGS: change these in ONE place ================= */
window.PSL_CONFIG = {
  FORM_ENDPOINT: '',   // URL that receives every lead (Google Apps Script / Formspree / Zapier). Empty = leads are NOT sent anywhere.
  GROUP_URL: '',       // WhatsApp community group invite link (optional)
  WHATSAPP: '918904820166',
  INSTAGRAM: 'https://www.instagram.com/drmariapramila/'
};
/* ======================================================================= */

(function () {
  var C = window.PSL_CONFIG;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (h) { return String(h == null ? '' : h).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;'); };
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion:reduce)').matches;
  var fine = window.matchMedia && matchMedia('(pointer:fine)').matches;

  /* ---------- navigation ---------- */
  var nav = $('#nav'), burger = $('#burger'), body = document.body;
  function setOpen(o) { nav.classList.toggle('open', o); body.classList.toggle('nav-open', o); body.style.overflow = o ? 'hidden' : ''; burger.setAttribute('aria-expanded', o); }
  if (nav && burger) {
    burger.addEventListener('click', function () { setOpen(!nav.classList.contains('open')); });
    $$('li > button', nav).forEach(function (b) {
      b.addEventListener('click', function () {
        var li = b.parentNode, was = li.classList.contains('open');
        $$('li.open', nav).forEach(function (x) { x.classList.remove('open'); x.querySelector('button').setAttribute('aria-expanded', false); });
        if (!was) { li.classList.add('open'); b.setAttribute('aria-expanded', true); }
      });
    });
    $$('a', nav).forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
    document.addEventListener('click', function (e) { if (window.innerWidth > 900 && !e.target.closest('.nav')) $$('li.open', nav).forEach(function (x) { x.classList.remove('open'); }); });
    window.addEventListener('resize', function () { if (window.innerWidth > 900) setOpen(false); });
  }
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { if (nav) setOpen(false); closeReel(); } });

  /* ---------- scroll reveal, progress bar, sticky bar ---------- */
  var els = $$('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: .06, rootMargin: '0px 0px -30px 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else els.forEach(function (el) { el.classList.add('in'); });
  var pg = $('#progress'), stick = $('#stick');
  window.addEventListener('scroll', function () {
    var h = document.documentElement;
    if (pg) pg.style.width = (h.scrollTop / Math.max(1, h.scrollHeight - h.clientHeight) * 100) + '%';
    if (stick) stick.classList.toggle('show', window.scrollY > 650);
  }, { passive: true });

  /* ---------- count up numbers, rotating hero word ---------- */
  var cu = $$('[data-count]');
  function run(el) { var t = +el.dataset.count, suf = el.dataset.suf || '', t0 = performance.now(); (function f(n) { var p = Math.min(1, (n - t0) / 1400), v = Math.round(t * (1 - Math.pow(1 - p, 3))); el.textContent = v.toLocaleString('en-IN') + suf; if (p < 1) requestAnimationFrame(f); })(t0); }
  if ('IntersectionObserver' in window) { var io2 = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { run(e.target); io2.unobserve(e.target); } }); }, { threshold: .6 }); cu.forEach(function (x) { io2.observe(x); }); }
  var rt = $('#rot'), words = ['retirement', 'my family’s protection', 'wealth creation', 'my child’s future', 'extra income', 'financial clarity'], wi = 0;
  if (rt && !reduce) setInterval(function () { rt.classList.add('sw'); setTimeout(function () { wi = (wi + 1) % words.length; rt.textContent = words[wi]; rt.classList.remove('sw'); }, 250); }, 2200);
  if (fine) $$('.path,.tier,.tool').forEach(function (c) { c.addEventListener('mousemove', function (e) { var r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5; c.style.transform = 'perspective(800px) rotateX(' + (-y * 6) + 'deg) rotateY(' + (x * 6) + 'deg) translateY(-6px)'; }); c.addEventListener('mouseleave', function () { c.style.transform = ''; }); });

  /* ---------- confetti ---------- */
  function confetti() { if (reduce) return; var cl = ['#D09C32', '#E8BC5A', '#011D43', '#1F8A63', '#fff']; for (var i = 0; i < 50; i++) { var d = document.createElement('i'); d.className = 'confetti'; d.style.left = Math.random() * 100 + 'vw'; d.style.background = cl[i % 5]; d.style.setProperty('--dx', (Math.random() * 200 - 100) + 'px'); d.style.animationDelay = Math.random() * .4 + 's'; document.body.appendChild(d); setTimeout(function (x) { x.remove(); }, 3000, d); } }

  /* ---------- THE shared lead form (used on every page) ---------- */
  var INTERESTS = ['Financial clarity', 'Retirement planning', 'Protecting my family (insurance)', 'Growing wealth', 'Earning extra income', 'Kids and youth financial literacy', 'Becoming an advisor', 'Joining the community', 'A workshop for my organisation', 'Something else'];
  var TIMES = ['Morning 9 AM to 12 PM', 'Afternoon 12 PM to 4 PM', 'Evening 4 PM to 7 PM'];
  function sendLead(data) {
    try { var a = JSON.parse(localStorage.getItem('psl_leads') || '[]'); a.push(data); localStorage.setItem('psl_leads', JSON.stringify(a)); } catch (x) { }
    if (C.FORM_ENDPOINT) { var fd = new FormData(); Object.keys(data).forEach(function (k) { fd.append(k, data[k]); }); try { fetch(C.FORM_ENDPOINT, { method: 'POST', body: fd, mode: 'no-cors' }); } catch (x) { } }
    else if (window.console) console.warn('PSL_CONFIG.FORM_ENDPOINT is empty: this lead was NOT sent anywhere.', data);
  }
  function renderForm(el, o) {
    o = o || {};
    var interest = o.interest || el.dataset.interest || '', list = INTERESTS.slice();
    if (interest && list.indexOf(interest) < 0) list.unshift(interest);
    var id = 'pf' + Math.random().toString(36).slice(2, 7);
    el.innerHTML =
      '<form class="pform" novalidate>' +
      '<h3>' + esc(o.title || el.dataset.title || 'Book a Free Slot') + '</h3>' +
      '<p class="ph">' + esc(o.sub || el.dataset.sub || 'Share your details and we will confirm a time with you. Takes under a minute.') + '</p>' +
      '<div class="pf-g"><label for="' + id + 'n">Full name<input id="' + id + 'n" name="name" autocomplete="name"></label>' +
      '<label for="' + id + 'm">Mobile / WhatsApp<input id="' + id + 'm" name="mobile" type="tel" inputmode="tel" autocomplete="tel"></label></div>' +
      '<div class="pf-g"><label for="' + id + 'e">Email (optional)<input id="' + id + 'e" name="email" type="email" autocomplete="email"></label>' +
      '<label for="' + id + 'c">City / Country<input id="' + id + 'c" name="city" autocomplete="address-level2"></label></div>' +
      '<label for="' + id + 'i">I am interested in<select id="' + id + 'i" name="interest">' + list.map(function (x) { return '<option' + (x === interest ? ' selected' : '') + '>' + esc(x) + '</option>'; }).join('') + '</select></label>' +
      '<label for="' + id + 't">Best time to call<select id="' + id + 't" name="time">' + TIMES.map(function (x) { return '<option>' + x + '</option>'; }).join('') + '</select></label>' +
      '<label class="pf-chk"><input type="checkbox" name="consent"><span>I agree to be contacted by Prosperity Life School. <a href="https://prosperitylifeschool.com/privacy-policy" target="_blank" rel="noopener">Privacy Policy</a> applies.</span></label>' +
      '<p class="pf-err" hidden>Please add your name, a valid mobile number and tick the box.</p>' +
      '<button class="btn lg" type="submit">' + esc(o.btn || el.dataset.btn || 'Book My Free Slot') + ' <svg class="ic"><use href="#i-arrow"/></svg></button>' +
      '<p class="pf-fine">Free · No obligation · We never share your details</p>' +
      '</form>';
    var f = $('form', el);
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = function (n) { return f.elements[n]; };
      var name = v('name').value.trim(), mob = v('mobile').value.trim(), d = mob.replace(/\D/g, '');
      var ok = name.length > 1 && /^[+0-9()\s-]+$/.test(mob) && d.length >= 8 && d.length <= 15 && v('consent').checked;
      $('.pf-err', f).hidden = ok; if (!ok) return;
      var q = new URLSearchParams(location.search);
      var data = {
        name: name, mobile: mob, email: v('email').value.trim(), city: v('city').value.trim(),
        interest: v('interest').value, call_time: v('time').value, contact_consent: 'Yes',
        source: o.source || el.dataset.source || document.title, page: location.href.split('?')[0].split('#')[0],
        utm_source: q.get('utm_source') || '', utm_medium: q.get('utm_medium') || '', utm_campaign: q.get('utm_campaign') || '', fbclid: q.get('fbclid') || '',
        submitted_at: new Date().toISOString()
      };
      if (o.extra) Object.keys(o.extra).forEach(function (k) { data[k] = o.extra[k]; });
      sendLead(data);
      var first = esc(name.split(' ')[0]);
      var wa = 'https://wa.me/' + C.WHATSAPP + '?text=' + encodeURIComponent('Hi, I am ' + name + '. I would like to talk about: ' + data.interest + '.');
      var group = (C.GROUP_URL && /community/i.test(data.interest)) ? '<a class="btn wab" href="' + esc(C.GROUP_URL) + '" target="_blank" rel="noopener"><svg class="ic" style="fill:#fff;stroke:none"><use href="#b-wa"/></svg>Join the WhatsApp Community</a>' : '';
      el.innerHTML = '<div class="pform pf-done"><div class="tick">✓</div><h3>Thank you, ' + first + '!</h3><p>We have your request and will contact you shortly to confirm your free slot.</p><div class="cta-row center">' + group + '<a class="btn wab" href="' + wa + '" target="_blank" rel="noopener"><svg class="ic" style="fill:#fff;stroke:none"><use href="#b-wa"/></svg>Message us on WhatsApp</a></div></div>';
      confetti();
    });
  }
  window.PSL = { renderForm: renderForm, sendLead: sendLead };
  $$('.pform-mount').forEach(function (el) { renderForm(el); });

  /* ---------- home: 2-question path finder, then the SAME shared form ---------- */
  var wb = $('#wzBody');
  if (wb) {
    var ic = { clar: '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>', ret: '<path d="M3 17h18M6 17a6 6 0 0112 0M12 4v3"/>', prot: '<path d="M12 3l8 3v6c0 4.5-3.2 7.6-8 9-4.8-1.4-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>', wealth: '<path d="M3 17l6-6 4 4 8-9"/><path d="M15 6h6v6"/>', inc: '<ellipse cx="9" cy="7" rx="6" ry="3"/><path d="M3 7v5c0 1.7 2.7 3 6 3"/><ellipse cx="16" cy="14" rx="5" ry="2.6"/>', kids: '<circle cx="9" cy="7" r="3"/><path d="M3 20v-2a5 5 0 015-5h2a5 5 0 015 5v2"/><circle cx="18" cy="9" r="2"/>', career: '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 012-2h2a2 2 0 012 2v2"/>', comm: '<circle cx="9" cy="8" r="3.2"/><circle cx="17" cy="9" r="2.4"/><path d="M3 20v-1.5A5 5 0 018 14h2a5 5 0 015 4.5V20"/>' };
    var G = [
      { k: 'clar', t: 'Understand my money (clarity)', s: 'Where I stand today', rec: 'Financial Clarity Assessment', href: 'prosperity-clarity-call-v5.html', i: 'Financial clarity', pts: ['See your gaps in saving, protection and debt', 'Plain-language results', 'Free 1-to-1 call to go through it'] },
      { k: 'ret', t: 'Plan my retirement', s: 'How much will I need?', rec: 'Retirement Clarity Call', href: 'prosperity-retirement-clarity-call.html', i: 'Retirement planning', pts: ['Know your retirement number', 'Check if your assets work together', 'Leave with your next 3 priorities'] },
      { k: 'prot', t: 'Protect my family', s: 'Insurance gaps', rec: 'Protection Gap Review', href: 'prosperity-protection-gap-review.html', i: 'Protecting my family (insurance)', pts: ['Check term, health and accident cover', 'Know waiting periods and limits', 'Clear, no-pressure review'] },
      { k: 'wealth', t: 'Grow my wealth', s: 'SIPs and goals', rec: 'Prosperity Clarity Call', href: 'prosperity-clarity-call-v5.html', i: 'Growing wealth', pts: ['Goal-based investment thinking', 'Match each goal to a timeline', 'Plain-language guidance'] },
      { k: 'inc', t: 'Earn extra income', s: 'Multiple income streams', rec: 'Advisor Career Readiness', href: 'prosperity-advisor-career-readiness.html', i: 'Earning extra income', pts: ['Find income paths that fit your skills', 'Practical, step-by-step approach', 'No quick-income promises'] },
      { k: 'kids', t: 'Teach my kids money', s: 'Ages 8 to 25', rec: 'Prosperity Clarity Call', href: 'prosperity-clarity-call-v5.html', i: 'Kids and youth financial literacy', pts: ['Age-wise programs: 8-13, 14-18, 19-25', 'Money habits for life', 'Parents guided too'] },
      { k: 'career', t: 'Build a finance career', s: 'Advisor or leader', rec: 'Advisor Career Readiness', href: 'prosperity-advisor-career-readiness.html', i: 'Becoming an advisor', pts: ['Check your readiness first', 'Training and mentoring', 'No guaranteed-income claims'] },
      { k: 'comm', t: 'Join the community', s: 'Learn with other families', rec: 'Prosperity Community', href: 'community.html', i: 'Joining the community', pts: ['Live weekly mentor calls', '16 money-mastery modules', 'Start with a free masterclass'] }
    ];
    var S = [['Just starting out', 'I want the basics'], ['Earning well, saving little', 'Money disappears by month end'], ['Planning bigger goals', 'Home, education, retirement'], ['Already well settled', 'I want structure and review']];
    var st = { step: 0 }, ws = $('#wzStep'), wbar = $('#wzBar');
    var wr = function () {
      var back = st.step > 0 ? '<button class="wzback" type="button" data-a="back">← Back</button>' : '';
      ws.textContent = 'Step ' + (st.step + 1) + ' of 3'; wbar.style.width = ((st.step + 1) / 3 * 100 * .9) + '%';
      var h = '';
      if (st.step === 0) h = '<h3>What would you like help with?</h3><p class="hint">Pick the one that matters most right now.</p><div class="wzopts">' + G.map(function (g, i) { return '<button class="wzo" type="button" data-g="' + i + '"><span class="wi"><svg viewBox="0 0 24 24">' + ic[g.k] + '</svg></span><span>' + g.t + '<small>' + g.s + '</small></span></button>'; }).join('') + '</div>';
      else if (st.step === 1) h = '<h3>Where are you right now?</h3><p class="hint">This helps us tailor your recommendation.</p><div class="wzopts">' + S.map(function (x, i) { return '<button class="wzo" type="button" data-s="' + i + '"><span>' + x[0] + '<small>' + x[1] + '</small></span></button>'; }).join('') + '</div>';
      else { var g = G[st.g]; h = '<h3>Great choice. Here is your match.</h3><div class="rec"><div class="rl">Recommended for you</div><h4>' + g.rec + '</h4><ul>' + g.pts.map(function (p) { return '<li>' + p + '</li>'; }).join('') + '</ul><a class="rec-link" href="' + g.href + '">See details →</a></div><div class="wz-form" id="wzForm"></div>'; }
      wb.innerHTML = h + (back ? '<div class="wzfoot">' + back + '</div>' : '');
      wb.style.animation = 'none'; void wb.offsetWidth; wb.style.animation = '';
      if (st.step === 2) renderForm($('#wzForm'), { interest: G[st.g].i, source: 'Home path finder', title: 'Book My Free Slot', sub: 'Leave your details and pick a time. We will confirm your slot.', extra: { money_stage: S[st.s][0], goal: G[st.g].t, recommended: G[st.g].rec } });
    };
    wb.addEventListener('click', function (ev) {
      var o = ev.target.closest('[data-g]'); if (o) { st.g = +o.dataset.g; st.step = 1; wr(); return; }
      o = ev.target.closest('[data-s]'); if (o) { st.s = +o.dataset.s; st.step = 2; wr(); return; }
      var a = ev.target.closest('[data-a]'); if (a && a.dataset.a === 'back') { st.step--; wr(); }
    });
    wr();
  }

  /* ---------- SIP illustration ---------- */
  var rs = $('#r_s');
  if (rs) {
    var ru = $('#r_u'), ry = $('#r_y');
    var fmt = function (n) { return n >= 1e7 ? '₹' + (n / 1e7).toFixed(2) + ' crore' : '₹' + (n / 1e5).toFixed(1) + ' lakh'; };
    var fv = function (start, step, years) { var r = 0.01, t = 0, m = start; for (var y = 0; y < years; y++) { for (var k = 0; k < 12; k++) t = (t + m) * (1 + r); m = m * (1 + step / 100); } return t; };
    var up = function () { var s = +rs.value, u = +ru.value, y = +ry.value; $('#v_s').textContent = '₹' + s.toLocaleString('en-IN'); $('#v_u').textContent = u + '%'; $('#v_y').textContent = y; $('#o_f').textContent = fmt(fv(10000, 0, y)); $('#o_u').textContent = fmt(fv(s, u, y)); };
    [rs, ru, ry].forEach(function (x) { x.addEventListener('input', up); }); up();
  }

  /* ---------- reels (videos are built into the page) ---------- */
  function reelSrc(n) { return (window.PSL_REELS && window.PSL_REELS[n]) || ('assets/reels/reel-' + n + '.mp4'); }
  $$('video[data-reel]').forEach(function (v) { v.src = reelSrc(v.dataset.reel); });
  if ('IntersectionObserver' in window) {
    var ro = new IntersectionObserver(function (es) { es.forEach(function (e) { var v = e.target; if (e.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () { }); } else v.pause(); }); }, { threshold: .5 });
    $$('.reel video').forEach(function (v) { ro.observe(v); });
  }
  var rm = $('#rmodal'), rvid = $('#rvid');
  function closeReel() { if (!rm || rm.hidden) return; rm.hidden = true; rvid.pause(); rvid.removeAttribute('src'); document.body.style.overflow = ''; }
  function openReel(card) {
    if (!rm) return; var n = card.dataset.n || card.querySelector('video').dataset.reel;
    rvid.onerror = function () { rm.hidden = true; rvid.removeAttribute('src'); window.open(C.INSTAGRAM, '_blank', 'noopener'); };
    rvid.src = reelSrc(n); rm.hidden = false; document.body.style.overflow = 'hidden'; var p = rvid.play(); if (p && p.catch) p.catch(function () { });
  }
  $$('.reel').forEach(function (c) { c.addEventListener('click', function () { openReel(c); }); c.addEventListener('keydown', function (e) { if (e.key === 'Enter') openReel(c); }); });
  if (rm) { $('#rx').addEventListener('click', closeReel); rm.addEventListener('click', function (e) { if (e.target === rm) closeReel(); }); $$('#rmodal a').forEach(function (a) { a.addEventListener('click', closeReel); }); }

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
