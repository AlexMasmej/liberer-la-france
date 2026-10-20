'use strict';
const money = n => new Intl.NumberFormat('fr-FR',{style:'currency',currency:'EUR',maximumFractionDigits:0}).format(n);
function rateAt(year){return year<2?.005:year<4?.01:year<6?.02:year<8?.03:.04;}
function project(gross,years,annual){
  const monthly=Math.pow(1+annual/100,1/12)-1;
  let balance=0,paid=0;
  for(let m=0;m<years*12;m++){
    const payment=gross*rateAt(Math.floor(m/12));
    balance=balance*(1+monthly)+payment;paid+=payment;
  }
  return {balance,paid,last:gross*rateAt(years-1)};
}
function update(){
  const gross=Number(document.querySelector('#gross').value),years=Number(document.querySelector('#years').value),r=Number(document.querySelector('#return').value);
  document.querySelector('#gross-value').textContent=money(gross);
  document.querySelector('#years-value').textContent=years+(years===1?' an':' ans');
  document.querySelector('#return-value').textContent=r.toLocaleString('fr-FR')+' %';
  const p=project(gross,years,r);
  document.querySelector('#capital').textContent=money(p.balance);
  document.querySelector('#paid').textContent=money(p.paid);
  document.querySelector('#monthly').textContent=money(p.last);
  const target=document.querySelector('#scenarios');target.replaceChildren();
  for(const rate of [-2,0,3]){
    const el=document.createElement('p'),b=document.createElement('b');
    b.textContent=money(project(gross,years,rate).balance);el.append(b,document.createTextNode('À '+rate+' % réel annuel net de frais'));target.append(el);
  }
}
document.querySelectorAll('.calculator input').forEach(el=>el.addEventListener('input',update));update();
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
function progress(){const available=document.documentElement.scrollHeight-innerHeight;document.querySelector('#progress').style.width=(available>0?100*scrollY/available:0)+'%';}
document.addEventListener('scroll',progress,{passive:true});progress();
