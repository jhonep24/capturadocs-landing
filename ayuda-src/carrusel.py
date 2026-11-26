"""Carrusel «casilla por casilla»: la hoja oficial con un recuadro sobre la casilla que se explica.
El HTML que se genera aquí es una lista numerada (se lee sin JavaScript); CARRUSEL_JS la convierte en carrusel."""
import html

from carrusel_fpj6 import PASOS as PASOS_FPJ6, PAGINA

CARRUSEL = {
    'acta-derechos-capturado-fpj6': dict(
        pasos=PASOS_FPJ6,
        imgs={1: '../img/carrusel-fpj6-h1.jpg', 2: '../img/carrusel-fpj6-h2.jpg'},
        alts={1: 'Primera hoja del formato oficial FPJ-6 en blanco', 2: 'Segunda hoja del formato oficial FPJ-6 en blanco'},
        pagina=PAGINA,
    ),
}

INTRO = ('<p>El <strong>recuadro dorado</strong> marca la parte de la hoja oficial que se explica en cada paso. '
         'Avanza con los botones, deslizando o con las teclas ← →.</p>')


def e(s):
    return html.escape(s, quote=True)


def carrusel(slug):
    c = CARRUSEL.get(slug)
    if not c:
        return ''
    pw, ph = c['pagina']
    lis = []
    for i, p in enumerate(c['pasos'], 1):
        caja = ''
        if p['caja']:
            x0, y0, x1, y1 = p['caja']
            x0, y0, x1, y1 = x0 - 3, y0 - 2, x1 + 3, y1 + 2  # un respiro para que el borde no tape el texto
            caja = ' data-caja="%.2f,%.2f,%.2f,%.2f"' % (x0 / pw * 100, y0 / ph * 100, (x1 - x0) / pw * 100, (y1 - y0) / ph * 100)
        ej = f'<p class="carr-ej"><strong>Ejemplo:</strong> {e(p["ej"])}</p>' if p.get('ej') else ''
        sug = f'<p class="carr-sug"><strong>Sugerencia:</strong> {e(p["sug"])}</p>' if p.get('sug') else ''
        lis.append(f'<li data-h="{p["h"]}"{caja}><h3>{e(p["t"])}</h3><p>{p["texto"]}</p>{ej}{sug}</li>')
    imgs = ' '.join(f'data-img{h}="{e(src)}" data-alt{h}="{e(c["alts"][h])}"' for h, src in c['imgs'].items())
    return (f'<div class="carr" {imgs} data-pw="{pw}" data-ph="{ph}" tabindex="0" role="region" aria-roledescription="carrusel" '
            f'aria-label="Paso a paso casilla por casilla">{INTRO}<ol class="carr-lista">{"".join(lis)}</ol></div>')


CARRUSEL_JS = r"""<script>(function(){
document.querySelectorAll('.carr').forEach(function(root){
var li=[].slice.call(root.querySelectorAll('.carr-lista>li')),n=li.length,pw=+root.dataset.pw,ph=+root.dataset.ph,cur=0;
if(!n)return;
function el(t,c,h){var x=document.createElement(t);if(c)x.className=c;if(h!=null)x.innerHTML=h;return x;}
function add(p){for(var i=1;i<arguments.length;i++)p.appendChild(arguments[i]);return p;}
var ui=el('div','carr-ui'),esc=el('div','carr-escena'),pila=el('div','carr-pila'),papel=el('div','carr-papel');
var vis=el('div','carr-vis'),hoja=el('div','carr-hoja'),caja=el('div','carr-caja'),pin=el('span','carr-pin'),imgs={};
[1,2].forEach(function(h){var s=root.getAttribute('data-img'+h);if(!s)return;var im=new Image();im.src=s;im.alt=root.getAttribute('data-alt'+h)||'';im.decoding='async';im.draggable=false;imgs[h]=im;hoja.appendChild(im);});
add(hoja,caja,pin);add(vis,hoja);add(papel,vis);
add(pila,el('div','carr-atras a1'),el('div','carr-atras a2'),papel);
add(esc,el('div','carr-luz'),pila);
var info=el('div','carr-info'),top=el('div','carr-top'),cnt=el('span','carr-cnt'),bar=el('div','carr-bar','<i></i>');
add(top,cnt,bar);
var card=el('div','carr-card');card.setAttribute('aria-live','polite');
var nav=el('div','carr-nav'),prev=el('button','carr-b','← Anterior'),next=el('button','carr-b carr-b2','Siguiente →');
prev.type=next.type='button';add(nav,prev,next);
var ir=el('label','carr-ir','Ir al paso: '),sel=el('select','carr-sel');sel.setAttribute('aria-label','Ir a un paso');
li.forEach(function(x,i){var o=document.createElement('option');o.value=i;o.textContent=(i+1)+'. '+x.querySelector('h3').textContent;sel.appendChild(o);});
add(ir,sel);add(info,top,card,nav,ir);add(ui,esc,info);
root.appendChild(ui);root.classList.add('on');
function clamp(v,a,b){return Math.max(a,Math.min(b,v));}
function enfocar(){
 var st=li[cur],h=+st.dataset.h,c=st.dataset.caja,W=vis.clientWidth;if(!W)return;
 var H=Math.round(clamp(W<520?W*0.95:W*0.72,270,540));vis.style.height=H+'px';
 Object.keys(imgs).forEach(function(k){imgs[k].style.display=(+k===h)?'block':'none';});
 var sMin=W<520?2.0:1.0,s=1,tx=0,ty=0;
 if(c){
  var b=c.split(',').map(Number),bx=b[0]/100,by=b[1]/100,bw=b[2]/100,bh=b[3]/100;
  var pxw=bw*W,pxh=bh*W*ph/pw;
  s=clamp(Math.min(0.94*W/pxw,0.78*H/pxh),sMin,3.2);
  var Wp=W*s,Hp=Wp*ph/pw;
  tx=(bw*Wp>W*0.9)?(-bx*Wp+0.03*W):(W/2-(bx+bw/2)*Wp);
  ty=H/2-(by+bh/2)*Hp;
  tx=clamp(tx,W-Wp,0);ty=clamp(ty,H-Hp,0);
  caja.style.cssText='display:block;left:'+b[0]+'%;top:'+b[1]+'%;width:'+b[2]+'%;height:'+b[3]+'%';
  pin.style.cssText='display:grid;left:'+b[0]+'%;top:'+b[1]+'%';
 }else{caja.style.display='none';pin.style.display='none';}
 hoja.style.width=(W*s)+'px';hoja.style.transform='translate('+tx+'px,'+ty+'px)';
}
function ver(i){
 cur=clamp(i,0,n-1);var st=li[cur];
 card.innerHTML='<div class="carr-hd"><b>'+(cur+1)+'</b><h3>'+st.querySelector('h3').innerHTML+'</h3></div>'+[].slice.call(st.children).slice(1).map(function(x){return x.outerHTML;}).join('');
 pin.textContent=cur+1;
 cnt.textContent='Paso '+(cur+1)+' de '+n;bar.firstChild.style.width=((cur+1)*100/n)+'%';
 prev.disabled=cur===0;next.disabled=cur===n-1;sel.value=cur;enfocar();
}
prev.addEventListener('click',function(){ver(cur-1);});next.addEventListener('click',function(){ver(cur+1);});
sel.addEventListener('change',function(){ver(+sel.value);});
root.addEventListener('keydown',function(ev){if(ev.target===sel)return;if(ev.key==='ArrowRight'){ver(cur+1);ev.preventDefault();}else if(ev.key==='ArrowLeft'){ver(cur-1);ev.preventDefault();}});
var x0=null,y0=null;
esc.addEventListener('touchstart',function(ev){var t=ev.changedTouches[0];x0=t.clientX;y0=t.clientY;},{passive:true});
esc.addEventListener('touchend',function(ev){if(x0===null)return;var t=ev.changedTouches[0],dx=t.clientX-x0,dy=t.clientY-y0;x0=null;
 if(Math.abs(dx)>50&&Math.abs(dx)>Math.abs(dy)*1.5)ver(cur+(dx<0?1:-1));},{passive:true});
var rz;window.addEventListener('resize',function(){clearTimeout(rz);rz=setTimeout(enfocar,120);});
Object.keys(imgs).forEach(function(k){imgs[k].addEventListener('load',enfocar);});
ver(0);
});})();</script>"""
