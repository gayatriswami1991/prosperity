/* Prosperity Life School: main-site extras (reveal, counters, home path-finder, SIP, reels, membership links). */
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

(function () {
  var C = window.PSL_CONFIG;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (h) { return String(h == null ? '' : h).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;'); };
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion:reduce)').matches;
  var fine = window.matchMedia && matchMedia('(pointer:fine)').matches;

  /* ---------- scroll reveal, progress bar, sticky bar ---------- */
  var els = $$('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: .06, rootMargin: '0px 0px -30px 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else els.forEach(function (el) { el.classList.add('in'); });
  /* ---------- count up numbers, rotating hero word ---------- */
  var cu = $$('[data-count]');
  function run(el) { var t = +el.dataset.count, suf = el.dataset.suf || '', t0 = performance.now(); (function f(n) { var p = Math.min(1, (n - t0) / 1400), v = Math.round(t * (1 - Math.pow(1 - p, 3))); el.textContent = v.toLocaleString('en-IN') + suf; if (p < 1) requestAnimationFrame(f); })(t0); }
  if ('IntersectionObserver' in window) { var io2 = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { run(e.target); io2.unobserve(e.target); } }); }, { threshold: .6 }); cu.forEach(function (x) { io2.observe(x); }); }
  var rt = $('#rot'), words = ['retirement', 'my family’s protection', 'wealth creation', 'my child’s future', 'extra income', 'financial clarity'], wi = 0;
  if (rt && !reduce) setInterval(function () { rt.classList.add('sw'); setTimeout(function () { wi = (wi + 1) % words.length; rt.textContent = words[wi]; rt.classList.remove('sw'); }, 250); }, 2200);
  if (fine) $$('.path,.tier,.tool').forEach(function (c) { c.addEventListener('mousemove', function (e) { var r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5; c.style.transform = 'perspective(800px) rotateX(' + (-y * 6) + 'deg) rotateY(' + (x * 6) + 'deg) translateY(-6px)'; }); c.addEventListener('mouseleave', function () { c.style.transform = ''; }); });

  /* membership buttons: use the Drive link when set, else keep the fallback href */
  $$('[data-link]').forEach(function (a) {
    var u = ((window.PSL_CONFIG || {}).LINKS || {})[a.dataset.link];
    if (u) { a.href = u; a.target = '_blank'; a.rel = 'noopener'; a.hidden = false; }
  });

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
      else { var g = G[st.g]; h = '<h3>Great choice. Here is your match.</h3><div class="rec"><div class="rl">Recommended for you</div><h4>' + g.rec + '</h4><ul>' + g.pts.map(function (p) { return '<li>' + p + '</li>'; }).join('') + '</ul><a class="rec-link" href="' + g.href + '">See details →</a></div><div class="wz-form" id="wzForm">' + ((document.getElementById('pslFormTpl') || {}).innerHTML || '') + '</div>'; }
      wb.innerHTML = h + (back ? '<div class="wzfoot">' + back + '</div>' : '');
      wb.style.animation = 'none'; void wb.offsetWidth; wb.style.animation = '';
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
  function reelSrc(n) { return 'assets/reels/reel-' + n + '.mp4'; }
  function prevSrc(n) { return 'assets/reels/preview-' + n + '.mp4'; }
  var lazyV = $$('video[data-reel]');
  if ('IntersectionObserver' in window) {
    var lo = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.src = prevSrc(e.target.dataset.reel); lo.unobserve(e.target); } }); }, { rootMargin: '300px' });
    lazyV.forEach(function (v) { lo.observe(v); });
  } else lazyV.forEach(function (v) { v.src = prevSrc(v.dataset.reel); });
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
})();
