// Datos de contacto compartidos por todas las páginas del sitio.
// Antes cada HTML tenía su propia copia del número (index, guia, seguridad);
// cambiarlo obligaba a acordarse de los tres. Ahora se cambia acá y ya.
// Se carga en el <head> de cada página, antes de cualquier script que lo use.
window.CAPTURADOCS = {
  WA_NUMBER: '573503593635',
  EMAIL: 'contacto@capturadocs.com',
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
