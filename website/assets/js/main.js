(function(){
  var body=document.body,nav=document.getElementById('nav'),burger=document.getElementById('burger');
  function setOpen(o){nav.classList.toggle('open',o);body.classList.toggle('nav-open',o);body.style.overflow=o?'hidden':'';burger.setAttribute('aria-expanded',o)}
  burger.addEventListener('click',function(){setOpen(!nav.classList.contains('open'))});
  nav.querySelectorAll('li > button').forEach(function(b){
    b.addEventListener('click',function(){
      var li=b.parentNode,was=li.classList.contains('open');
      nav.querySelectorAll('li.open').forEach(function(x){x.classList.remove('open');x.querySelector('button').setAttribute('aria-expanded',false)});
      if(!was){li.classList.add('open');b.setAttribute('aria-expanded',true)}
    });
  });
  document.addEventListener('click',function(e){if(window.innerWidth>900&&!e.target.closest('.nav'))nav.querySelectorAll('li.open').forEach(function(x){x.classList.remove('open')})});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){setOpen(false);nav.querySelectorAll('li.open').forEach(function(x){x.classList.remove('open')})}});
  window.addEventListener('resize',function(){if(window.innerWidth>900)setOpen(false)});
  var stick=document.getElementById('stick');
  if(stick){window.addEventListener('scroll',function(){stick.classList.toggle('show',window.scrollY>650)},{passive:true})}
  var els=document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.08,rootMargin:'0px 0px -40px 0px'});
    els.forEach(function(el){io.observe(el)});
  }else els.forEach(function(el){el.classList.add('in')});
})();
