# Centro de ayuda: páginas de práctica (errores, lista de chequeo, narración y uso desde el celular).
from c_flagrancia import LEY, LEY6

ERRORES = dict(
    slug='errores-comunes-informes-captura', grupo='practica', corto='Errores comunes', icono='triangle-alert',
    titulo='Errores comunes en el informe de captura en flagrancia y cómo evitarlos',
    desc='Los errores que más se repiten al diligenciar FPJ-5, 6, 7 y 8: datos que no coinciden, casillas vacías, descripciones distintas y firmas sin fecha.',
    desc_card='Datos que no coinciden, casillas vacías y descripciones distintas.',
    kicker='Práctica', min=7,
    h1='Errores comunes en el informe de captura en flagrancia <em>y cómo evitarlos</em>',
    h1_plano='Errores comunes en el informe de captura en flagrancia y cómo evitarlos',
    lead='Casi todos los problemas de un informe de captura vienen de lo mismo: la misma información escrita de varias maneras. Estos son los diez errores más fáciles de cometer y cómo prevenirlos.',
    secciones=[
        ('por-que', 'Por qué un detalle pequeño se vuelve un problema', '''
<p>Una captura en flagrancia genera varios documentos que se leen juntos: el informe, el acta de derechos, el rótulo y la cadena de custodia. Cuando los datos no coinciden entre ellos, quien los revisa tiene que preguntarse cuál es el correcto, y eso obliga a corregir, repetir o aclarar. Lo grave no es el error en sí, sino que <strong>resta credibilidad al procedimiento</strong>.</p>
<p>La mayoría de las inconsistencias se producen por una razón sencilla: <strong>el mismo dato se escribe a mano varias veces</strong>. Cada vez que lo retipeas hay una oportunidad de cometer un error.</p>'''),
        ('diez', 'Los diez errores más comunes', '''
<div class="pasos">
<div class="paso"><b>1</b><div><h3>Nombre del capturado escrito distinto</h3><p>«Carlos Andrés Ramírez Díaz» en un formato y «Carlos A. Ramírez» en otro. Se evita copiándolo del documento una vez y reutilizándolo.</p></div></div>
<div class="paso"><b>2</b><div><h3>NUNC con un dígito cambiado</h3><p>El Número Único de Noticia Criminal debe ser idéntico en los cuatro formatos. Cópialo de una sola fuente.</p></div></div>
<div class="paso"><b>3</b><div><h3>Fecha y hora de la captura que no coinciden</h3><p>El FPJ-5 advierte que la fecha y hora de la captura deben coincidir con las registradas en el acta de derechos.</p></div></div>
<div class="paso"><b>4</b><div><h3>Fecha de nacimiento y edad en blanco o contradictorias</h3><p>Se piden en el FPJ-5, el FPJ-6 y la constancia de buen trato. Que la edad sea coherente con la fecha de nacimiento.</p></div></div>
<div class="paso"><b>5</b><div><h3>Descripción del elemento distinta entre formatos</h3><p>Lo que en el FPJ-5 es «celular negro» en el rótulo es «Samsung A14» y en la cadena de custodia otra cosa. Escríbela una vez y pégala igual.</p></div></div>
<div class="paso"><b>6</b><div><h3>Rótulo faltante o con varios elementos juntos</h3><p>Es un rótulo por elemento incautado, con su número de orden y su cantidad.</p></div></div>
<div class="paso"><b>7</b><div><h3>Marcas H, R y E sin correspondencia</h3><p>Una persona que firma en la cadena de custodia debe haber hallado, recolectado o embalado, y cada una de esas marcas tiene que corresponder con lo que pasó.</p></div></div>
<div class="paso"><b>8</b><div><h3>Firmas sin fecha o espacios de firma vacíos</h3><p>La cadena de custodia registra a cada persona que tuvo contacto con el elemento; sin fecha, el tramo queda sin soporte.</p></div></div>
<div class="paso"><b>9</b><div><h3>Narración con opiniones en lugar de hechos</h3><p>El formato pide una narración «cronológica y concreta». Describe lo que se vio y se hizo, en orden, sin adjetivos.</p></div></div>
<div class="paso"><b>10</b><div><h3>Anexos que no se adjuntan</h3><p>El informe lista los anexos (acta de derechos, cadena de custodia, rótulo). Si los nombras, tienen que estar.</p></div></div></div>'''),
        ('prevenir', 'Cómo prevenirlos', '''
<ul>
<li><strong>Escribe cada dato una sola vez</strong> y reutilízalo en los demás documentos.</li>
<li><strong>Revisa con una lista</strong> antes de firmar: la <a href="lista-de-chequeo-captura-flagrancia.html">lista de chequeo</a> reúne los puntos de este artículo para imprimir.</li>
<li><strong>Lee los documentos juntos</strong>, uno al lado del otro, buscando solo las coincidencias de nombre, documento, fecha, hora y descripción.</li>
<li><strong>Verifica con el documento físico</strong> los datos personales, no de memoria ni de un mensaje.</li></ul>
<div class="tip"><p><strong>Una forma de evitar los diez a la vez:</strong> llenar un solo formulario y generar los cuatro documentos desde ahí. Así el nombre, el NUNC, la fecha y la descripción son los mismos por construcción. Es lo que hace CapturaDocs Express.</p></div>'''),
    ],
    faq=[
        ('¿Cuál es el error más frecuente en un informe de captura?', 'La inconsistencia de datos entre los formatos: el nombre, el documento, la fecha y la hora o la descripción del elemento escritos de manera distinta en el informe, el acta, el rótulo y la cadena de custodia.'),
        ('¿La fecha y hora de la captura deben coincidir entre documentos?', 'Sí. El propio FPJ-5 advierte debajo del campo de fecha y hora de la captura que esos datos deben coincidir con los registrados en el acta de derechos del capturado.'),
        ('¿Cuántos rótulos hay que llenar?', 'Uno por cada elemento material probatorio o evidencia física incautada.'),
        ('¿Cómo evito los errores de transcripción?', 'Escribiendo cada dato una sola vez y reutilizándolo, y revisando los documentos juntos antes de firmar. Una herramienta como CapturaDocs Express automatiza la reutilización.'),
    ],
    rel=['lista-de-chequeo-captura-flagrancia', 'como-redactar-la-narracion-de-los-hechos', 'informe-captura-flagrancia-fpj5'],
    fuentes=['Formatos FPJ-5, FPJ-6, FPJ-7 y FPJ-8 (advertencias impresas en los mismos formatos).', 'Ley 906 de 2004, art. 254: ' + LEY6 + '.'],
)

CHEQUEO_ITEMS = [
    ('Todos los formatos', [
        'El NUNC es el mismo en FPJ-5, FPJ-6, FPJ-7 y FPJ-8.',
        'Nombres y apellidos del capturado escritos igual en todos.',
        'Tipo y número de documento iguales en todos.',
        'Fecha y hora de la captura iguales en el informe y en el acta de derechos.',
        'Letra legible o texto digitado, sin tachones.']),
    ('FPJ-5 · Informe de Captura', [
        'Destino del informe y presunta conducta punible con su artículo.',
        'Lugar de los hechos completo (dirección, barrio, localidad, municipio).',
        'Datos del capturado completos, con edad y fecha de nacimiento coherentes.',
        'Víctimas y testigos, si los hay, con su contacto.',
        'Descripción de los elementos recolectados.',
        'Narración cronológica y concreta, sin opiniones.',
        'Fecha y hora en que se pone a disposición del fiscal.',
        'Anexos listados y adjuntos; datos del servidor y firma.']),
    ('FPJ-6 · Acta de Derechos', [
        'Fecha, hora y lugar de la lectura de derechos.',
        'Un acta por cada capturado.',
        'Persona a quien se comunica la captura (nombre, identificación, teléfono y hora).',
        'Firma y huella del capturado, o anotación en observaciones si no quiso firmar.',
        'Constancia de buen trato con los mismos datos del informe.']),
    ('FPJ-7 · Rótulo', [
        'Un rótulo por elemento, con número de orden y cantidad.',
        'Fecha y hora de recolección (hora en 24 horas).',
        'Dirección y ubicación específica del hallazgo.',
        'Nombre y documento de la persona a quien se le encontró el elemento.',
        'Descripción con marca, modelo, color, serial o IMEI si aplica.',
        'Quién diligencia el rótulo: nombre, cédula, entidad, cargo y firma.']),
    ('FPJ-8 · Cadena de Custodia', [
        'Una fila por cada persona que interviene, con sus marcas H, R y E correctas.',
        'Cédula, entidad y firma con fecha de cada una.',
        'Descripción igual a la del rótulo y a la del informe.',
        'Historia clínica solo si la entidad de salud recolectó el elemento.']),
]

def _chequeo_html():
    out = ['<p class="solo-pantalla">Marca cada punto en pantalla o <strong>imprime esta página</strong> y llévala al procedimiento.</p>',
           '<p><button type="button" class="btn-p" onclick="window.print()">Imprimir la lista</button></p>']
    n = 0
    for tit, items in CHEQUEO_ITEMS:
        out.append(f'<h3>{tit}</h3><ul class="chk">')
        for it in items:
            n += 1
            out.append(f'<li><label><input type="checkbox"/> <span>{it}</span></label></li>')
        out.append('</ul>')
    return ''.join(out)

CHEQUEO = dict(
    slug='lista-de-chequeo-captura-flagrancia', grupo='practica', corto='Lista de chequeo', icono='check',
    titulo='Lista de chequeo para el informe de captura en flagrancia (imprimible)',
    desc='Lista de chequeo imprimible para revisar el FPJ-5, FPJ-6, FPJ-7 y FPJ-8 antes de firmar: coincidencias de datos, casillas, firmas y anexos.',
    desc_card='Para imprimir y revisar los cuatro formatos antes de firmar.',
    kicker='Lista imprimible', min=4,
    h1='Lista de chequeo del informe de captura en flagrancia <em>(imprimible)</em>',
    h1_plano='Lista de chequeo del informe de captura en flagrancia (imprimible)',
    lead='Veintitantos puntos para revisar antes de firmar. Está pensada para los cuatro formatos juntos, porque es ahí donde se ven las diferencias.',
    secciones=[('lista', 'Antes de firmar y entregar', _chequeo_html())],
    faq=[
        ('¿Esta lista reemplaza el instructivo oficial?', 'No. Es una ayuda de revisión basada en lo que piden los formatos y en lo que se repite como error. Para cualquier duda manda el instructivo vigente y la orientación de tu fiscal o tu superior.'),
        ('¿Puedo imprimirla?', 'Sí. Usa el botón «Imprimir la lista» o la opción de imprimir de tu navegador; está preparada para que salga en una o dos hojas.'),
    ],
    rel=['errores-comunes-informes-captura', 'informe-captura-flagrancia-fpj5', 'cadena-de-custodia-fpj8'],
    extra_css='''.chk{list-style:none;display:grid;gap:4px;padding:0!important}
.chk li{padding-left:0!important}.chk li::before{display:none!important}
.chk label{display:flex;gap:12px;align-items:flex-start;padding:10px 12px;border-radius:10px;cursor:pointer;min-height:44px;border:1px solid transparent}
.chk label:hover{background:rgba(240,165,0,.08);border-color:rgba(240,165,0,.3)}
.chk input{width:22px;height:22px;margin-top:2px;accent-color:#f0a500;flex:none}
.chk input:checked+span{color:var(--muted);text-decoration:line-through}
@media print{nav,.hero,.toc,.cta,.producto,.faq,.rel,footer,.btn-p,.solo-pantalla,.aviso{display:none!important}
 body{background:#fff;color:#000}article h2,article h3{color:#000}.chk label{color:#000;border:0;padding:3px 0;min-height:0}.chk input{accent-color:#000}
 .chk input:checked+span{color:#000;text-decoration:none}article section{padding:0}}''',
    fuentes=['Formatos FPJ-5, FPJ-6, FPJ-7 y FPJ-8 y artículos 254 y 303 de la Ley 906 de 2004: ' + LEY + '.'],
)

NARRACION = dict(
    slug='como-redactar-la-narracion-de-los-hechos', grupo='practica', corto='Narración de los hechos', icono='pen-line',
    titulo='Cómo redactar la narración de los hechos de un informe de captura',
    desc='Cómo escribir la narración de los hechos del FPJ-5: orden cronológico, qué incluir, plantilla con ejemplo y las frases que conviene evitar.',
    desc_card='Orden, plantilla y ejemplo para redactar sin opiniones.',
    kicker='Redacción', min=8,
    h1='Cómo redactar la narración de los hechos <em>de un informe de captura</em>',
    h1_plano='Cómo redactar la narración de los hechos de un informe de captura',
    lead='La narración es la parte del FPJ-5 que más tiempo toma y la que más pesa. Una forma ordenada de escribirla, con una plantilla y un ejemplo inventado.',
    secciones=[
        ('que-pide', 'Qué pide el formato', '''
<p>La sección 9 del <a href="informe-captura-flagrancia-fpj5.html">Informe de Captura (FPJ-5)</a> se titula «Narración de los hechos (en forma cronológica y concreta)». Eso significa dos cosas: que <strong>sigue el orden en que ocurrieron las cosas</strong>, y que <strong>cuenta hechos concretos</strong>, no impresiones.</p>
<p>La narración tiene un lector con un propósito: la Fiscalía necesita entender qué pasó, por qué se actuó y cómo se garantizaron los derechos para decidir cómo presentar el caso (art. 302 del Código de Procedimiento Penal).</p>'''),
        ('orden', 'El orden que funciona', '''
<ol class="lista">
<li><strong>Quién y cuándo.</strong> Quién narra y en qué circunstancias estaba (patrullaje, atención de llamado, etc.), con fecha, hora y lugar.</li>
<li><strong>Qué se percibió.</strong> Lo que se vio o se oyó, o lo que informó la víctima o un tercero, citando quién lo dijo.</li>
<li><strong>Cómo se individualizó a la persona.</strong> Por qué se la identificó como autora o partícipe: por señalamiento, por persecución, por los objetos que tenía, por una grabación o por el vehículo en que se desplazaba (las situaciones del artículo 301).</li>
<li><strong>La aprehensión.</strong> Cómo se produjo, a qué hora y en qué lugar exactos.</li>
<li><strong>Los derechos.</strong> Que se le informaron de manera inmediata (art. 303) y a qué hora.</li>
<li><strong>Los elementos.</strong> Qué se halló, en dónde, quién lo recolectó y lo embaló.</li>
<li><strong>El traslado.</strong> Adónde se condujo y a qué hora se puso a disposición del fiscal.</li></ol>'''),
        ('plantilla', 'Plantilla con un ejemplo inventado', '''
<div class="norma"><h3>Ejemplo (hechos y nombres inventados)</h3>
<p>«El día 16 de octubre de 2026, siendo las 14:30 horas, en desarrollo de patrullaje por la carrera 7 con calle 45, en la localidad de Chapinero, el suscrito patrullero fue abordado por una persona que informó haber sido víctima del hurto de un teléfono celular y señaló a un hombre que se alejaba del local comercial. Se realizó el seguimiento a pie por aproximadamente 100 metros y a las 14:35 horas se le dio alcance, identificándolo con la cédula de ciudadanía 1.020.345.678 como Carlos Andrés Ramírez Díaz. En el bolsillo derecho del pantalón se le encontró un celular marca Samsung Galaxy A14 de color negro, que la víctima reconoció como suyo. A las 14:40 horas se le informaron sus derechos conforme al artículo 303 del C.P.P. y se diligenció el acta correspondiente. El elemento fue embalado y rotulado por el suscrito. A las 15:10 horas fue conducido a la URI y puesto a disposición del fiscal de turno.»</p></div>
<p>Observa lo que tiene este ejemplo: <strong>horas puntuales</strong>, <strong>acciones verificables</strong>, <strong>una fuente para cada dato</strong> (la víctima señaló, el patrullero siguió) y <strong>cada elemento nombrado igual que en el rótulo</strong>.</p>'''),
        ('evitar', 'Lo que conviene evitar', '''
<div class="tabla"><table><thead><tr><th>Evita</th><th>Mejor así</th></tr></thead><tbody>
<tr><td>«Un sujeto de pésima actitud»</td><td>«La persona, al ver a la patrulla, aceleró el paso y botó una bolsa al suelo.»</td></tr>
<tr><td>«Se encontraba cometiendo un hurto» (sin decir qué se vio)</td><td>«Se observó que la persona sacó un celular del bolso de la víctima.»</td></tr>
<tr><td>«Aproximadamente por la tarde»</td><td>«A las 14:30 horas.»</td></tr>
<tr><td>«Se le informaron sus derechos» (sin hora)</td><td>«A las 14:40 horas se le informaron sus derechos y se diligenció el acta.»</td></tr>
<tr><td>Dos descripciones distintas del mismo elemento</td><td>La misma descripción del rótulo y de la cadena de custodia.</td></tr></tbody></table></div>
<div class="tip"><p><strong>Consejo:</strong> antes de escribir, anota las horas y los datos en el orden de arriba. Escribir el relato desde esas notas toma la mitad del tiempo y evita contradicciones.</p></div>'''),
    ],
    faq=[
        ('¿Qué extensión debe tener la narración?', 'La que haga falta para que sea concreta y completa. El formato permite ampliar el espacio cuantas veces sea necesario, pero no se trata de escribir más sino de dejar claros los hechos en orden.'),
        ('¿Debo narrar en primera o en tercera persona?', 'Cualquiera de las dos sirve mientras seas consistente en todo el relato. Lo importante es que sea cronológico y concreto.'),
        ('¿Debo incluir lo que dijeron la víctima o los testigos?', 'Sí, cuando es la base de la individualización o de la aprehensión, indicando quién lo dijo. Evita reproducir opiniones o conjeturas.'),
        ('¿La narración debe coincidir con los demás formatos?', 'Sí. Las fechas, horas, nombres y la descripción de los elementos de la narración deben ser iguales a los del acta de derechos, el rótulo y la cadena de custodia.'),
    ],
    rel=['informe-captura-flagrancia-fpj5', 'errores-comunes-informes-captura', 'captura-en-flagrancia-colombia'],
    fuentes=['Formato FPJ-5, sección 9.', 'Ley 906 de 2004, arts. 301, 302 y 303: ' + LEY + '.'],
)

CELULAR = dict(
    slug='informe-de-captura-desde-el-celular', grupo='practica', corto='Desde el celular', icono='smartphone',
    titulo='Informe de captura desde el celular: Android, iPhone y computador',
    desc='Cómo diligenciar el informe de captura en flagrancia desde el celular o el computador y generar el FPJ-5, 6, 7 y 8 con un solo formulario, incluso sin conexión.',
    desc_card='Llenar un solo formulario y generar los cuatro formatos.',
    kicker='Herramienta', min=5,
    h1='Informe de captura desde el celular: <em>un formulario, todos los documentos</em>',
    h1_plano='Informe de captura desde el celular: un formulario, todos los documentos',
    lead='Escribir a mano cuatro formatos que repiten los mismos datos es lento y propenso a errores. Así funciona hacerlo desde el celular o el computador con CapturaDocs Express.',
    cta_t='Pruébalo con tu próximo caso',
    cta_p='Tienes 5 casos completos gratis, sin tarjeta y sin registro obligatorio. Funciona en Windows, Android e iPhone.',
    secciones=[
        ('problema', 'El problema de llenar los formatos a mano', '''
<p>Los formatos FPJ-5, FPJ-6, FPJ-7 y FPJ-8 piden varias veces los mismos datos: NUNC, nombres, documento, fecha y hora, lugar y descripción de los elementos. Escribirlos a mano o en Word cuatro veces cuesta tiempo y deja espacio para el error: <a href="errores-comunes-informes-captura.html">el nombre que cambia, la hora que no coincide, la descripción distinta</a>.</p>'''),
        ('como', 'Cómo funciona', '''
<div class="pasos">
<div class="paso"><b>1</b><div><h3>Diligencias el caso una sola vez</h3><p>Un solo formulario por pasos: encabezado, capturado, policías, elementos incautados y hechos.</p></div></div>
<div class="paso"><b>2</b><div><h3>La aplicación valida</h3><p>Avisa lo que falta o no cuadra antes de generar, para que no tengas que descubrirlo después.</p></div></div>
<div class="paso"><b>3</b><div><h3>Generas los documentos</h3><p>Sale el Informe de Captura (FPJ-5), el Acta de Derechos (FPJ-6), el Rótulo (FPJ-7), la Cadena de Custodia (FPJ-8) y el Acta de Incautación, con el formato oficial.</p></div></div>
<div class="paso"><b>4</b><div><h3>Los compartes o los imprimes</h3><p>Por WhatsApp, correo o Drive desde el celular, o desde la carpeta del caso en el computador.</p></div></div></div>
<p>Puedes ver cómo quedan en la sección <a href="../index.html#documentos">«Documentos oficiales»</a> de la página principal y paso a paso en la <a href="../guia.html">guía de uso</a>.</p>'''),
        ('donde', 'Dónde funciona', '''
<ul>
<li><strong>Windows:</strong> instalador para el computador; los documentos quedan en una carpeta por caso.</li>
<li><strong>Android:</strong> aplicación instalable.</li>
<li><strong>iPhone:</strong> aplicación web que se agrega a la pantalla de inicio.</li>
<li><strong>Sin conexión:</strong> el formulario y la generación de documentos funcionan sin internet; el servidor propio se usa para verificar la licencia (y para la mejora de redacción con IA, solo si decides usarla).</li></ul>
<p>Cómo protegemos los datos: <a href="../seguridad.html">arquitectura de privacidad</a>.</p>'''),
        ('precio', 'Cuánto cuesta', '''
<div class="tabla"><table><thead><tr><th>Plan</th><th>Precio</th><th>Incluye</th></tr></thead><tbody>
<tr><td>Prueba gratuita</td><td>$0</td><td>5 casos completos, sin tarjeta.</td></tr>
<tr><td>Semanal</td><td>$12.000 COP</td><td>7 días, casos ilimitados, un dispositivo.</td></tr>
<tr><td>Mensual</td><td>$35.000 COP</td><td>30 días, casos ilimitados, mejora de redacción con IA.</td></tr>
<tr><td>Negocio/Estación</td><td>$100.000 COP</td><td>30 días, casos ilimitados, mejora de redacción con IA y soporte por WhatsApp (versión web de computador).</td></tr></tbody></table></div>
<p>Los precios vigentes están siempre en la <a href="../index.html#precios">página principal</a>.</p>'''),
    ],
    faq=[
        ('¿CapturaDocs Express es una aplicación oficial de la Policía Nacional?', 'No. Es una herramienta privada e independiente, no afiliada ni avalada por la Policía Nacional de Colombia. Facilita el diligenciamiento de los formatos.'),
        ('¿Funciona sin internet?', 'Sí. El formulario y la generación de los documentos funcionan sin conexión. La conexión se usa para verificar la licencia.'),
        ('¿Qué documentos genera?', 'El Informe de Captura (FPJ-5), el Acta de Derechos del Capturado (FPJ-6), el Rótulo (FPJ-7), el Registro de Cadena de Custodia (FPJ-8) y el Acta de Incautación.'),
        ('¿Cuánto cuesta probarlo?', 'La prueba es gratuita con 5 casos completos, sin tarjeta. Después hay licencia semanal ($12.000 COP), mensual ($35.000 COP) y Negocio/Estación ($100.000 COP).'),
    ],
    rel=['informe-captura-flagrancia-fpj5', 'errores-comunes-informes-captura', 'lista-de-chequeo-captura-flagrancia'],
    fuentes=[],
)
PAGINAS = [ERRORES, CHEQUEO, NARRACION, CELULAR]
