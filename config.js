// Datos de contacto compartidos por todas las páginas del sitio.
// Antes cada HTML tenía su propia copia del número (index, guia, seguridad);
// cambiarlo obligaba a acordarse de los tres. Ahora se cambia acá y ya.
// Se carga en el <head> de cada página, antes de cualquier script que lo use.
window.CAPTURADOCS = {
  WA_NUMBER: '573503593635',
  EMAIL: 'contacto@capturadocs.com',
  // Comentarios del Centro de ayuda. Vacío = la sección no aparece. Ver capturadocs-comentarios/ (Worker).
  COMENTARIOS_URL: 'https://capturadocs-comentarios.capturadocs.workers.dev',
  TURNSTILE_SITEKEY: '0x4AAAAAAGQ6d9TEtiYQbZMR',
  // Videos tutoriales de guia.html. Se pega aca el ID de 11 caracteres del
  // video de YouTube (lo que va despues de "v=" o de "youtu.be/"). Mientras un
  // ID este vacio, ese video NO aparece en la pagina: no hay huecos ni
  // portadas rotas. Ver GUIONES_VIDEOS.md.
  VIDEOS: {
    instalar: '',     // Instalar y primer ingreso      (seccion 1 de la guia)
    licencia: '',     // Activar la licencia            (seccion 3)
    diligenciar: '',  // Diligenciar un caso y generar  (seccion 4)
    rotulo: '',       // Archivos y rotulo al 60%       (seccion 6)
  },
};

// Contador privado de descargas (ver capturadocs-comentarios/). Solo cuenta clics en los enlaces de una lista fija
// (PDF en blanco, APK, .exe y app web); un fallo nunca interrumpe la descarga. Sin cookies ni IP.
(function () {
  document.addEventListener('click', function (ev) {
    try {
      var C = window.CAPTURADOCS, u = C.COMENTARIOS_URL;
      if (/^(localhost|127\.0\.0\.1)$/.test(location.hostname)) { var q = new URLSearchParams(location.search).get('comentarios'); if (q) u = q; }
      if (!u) return;
      var a = ev.target.closest && ev.target.closest('a[href]');
      if (!a) return;
      var h = a.getAttribute('href') || '', m, f = '';
      if ((m = h.match(/formato-fpj(\d)-en-blanco\.pdf(\?|$)/))) f = 'pdf-fpj' + m[1];
      else if (/CapturaDocs\.Express\.Android\.apk(\?|$)/.test(h)) f = 'app-apk';
      else if (/CapturaDocs\.Express\.Setup\.[\d.]+\.exe(\?|$)/.test(h)) f = 'app-exe';
      else if (/^https:\/\/capturadocs-app\.capturadocs\.workers\.dev/.test(h)) f = 'app-web';
      if (!f) return;
      fetch(u.replace(/\/+$/, '') + '/api/descarga', { method: 'POST', body: JSON.stringify({ f: f }), headers: { 'Content-Type': 'text/plain' }, keepalive: true }).catch(function () {});
    } catch (e) { /* sin contar */ }
  }, true);
})();
