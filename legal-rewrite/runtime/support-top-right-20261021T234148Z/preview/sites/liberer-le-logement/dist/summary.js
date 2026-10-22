'use strict';
const tip=document.querySelector('#definition');let active=null,hideTimer;
function closeTip(){
  clearTimeout(hideTimer);tip.hidden=true;
  if(active){active.setAttribute('aria-expanded','false');active.removeAttribute('aria-describedby');}
  active=null;
}
function showTip(el){
  closeTip();active=el;el.setAttribute('aria-expanded','true');el.setAttribute('aria-describedby','definition');
  tip.textContent=el.dataset.definition;tip.hidden=false;
}
function leaveTip(){
  clearTimeout(hideTimer);
  hideTimer=setTimeout(()=>{if(active&&!active.matches(':focus-visible'))closeTip();},300);
}
document.querySelectorAll('.term').forEach(el=>{
  let pointerType;
  el.addEventListener('pointerenter',e=>{if(e.pointerType==='mouse')showTip(el);});
  el.addEventListener('pointerleave',e=>{if(e.pointerType==='mouse')leaveTip();});
  el.addEventListener('pointerdown',e=>{pointerType=e.pointerType;});
  el.addEventListener('focus',()=>{if(el.matches(':focus-visible'))showTip(el);});
  el.addEventListener('blur',()=>{if(active===el)closeTip();});
  el.addEventListener('click',e=>{
    if(e.detail===0||(e.pointerType||pointerType)==='mouse')showTip(el);
    else if(active===el)closeTip();else showTip(el);
  });
});
tip.addEventListener('pointerenter',()=>clearTimeout(hideTimer));
tip.addEventListener('pointerleave',leaveTip);
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeTip();});
document.addEventListener('click',e=>{if(!e.target.closest('.term')&&!e.target.closest('#definition'))closeTip();});

if(/^#article-/.test(location.hash))location.replace('avant-projet.html'+location.hash);
