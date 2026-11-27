# Centro de ayuda: guía del FPJ-4 (Actuación del Primer Responsable). Página «suave»: la app se menciona como servicio extra,
# sin bloque comercial grande, porque el foco comercial del sitio es la captura en flagrancia.
# Las secciones salen del formato FPJ-4 V4 (aprobado 2022-07-26, CNPJ), leído del documento oficial.
FPJ4 = dict(
    slug='informe-primer-respondiente-fpj4', grupo='formatos', corto='Primer Responsable (FPJ-4)', icono='shield-check',
    titulo='FPJ-4: cómo diligenciar el Formato de Actuación del Primer Responsable, sección por sección',
    desc='Cómo llenar el FPJ 4 (FPJ4), Actuación del Primer Responsable: lugar de los hechos, protección del lugar, heridos, muertos, vehículos, capturados, testigos, relevo y constancia de recibido.',
    desc_card='Las 11 secciones del formato del primer responsable.',
    kicker='Formato FPJ-4', min=5, suave=True,
    actualizado='22 de noviembre de 2026', modificado='2026-11-22', publicado='2026-11-22',
    h1='Actuación del Primer Responsable FPJ-4: <em>cómo diligenciarlo</em>',
    h1_plano='Actuación del Primer Responsable FPJ-4: cómo diligenciarlo',
    lead='El FPJ-4 es el formato de actuación del primer responsable: deja constancia de lo que se encontró en el lugar de los hechos, de cómo se protegió y de a quién se entregó. Aquí está qué pide cada sección.',
    secciones=[
        ('que-es', '¿Qué es el FPJ-4 y cuándo se usa?', '''
<p>El <strong>Formato de Actuación del Primer Responsable (FPJ-4)</strong> es el documento del primer responsable de un hecho. Por lo que pregunta, su contenido es: <strong>si el lugar se acordonó, si hubo alteración, quién ingresó, qué elementos se recibieron de la ciudadanía, quiénes resultaron heridos o muertos, quién fue capturado y quién recibió el lugar</strong>.</p>
<p>No es lo mismo que el FPJ-5. El <a href="informe-captura-flagrancia-fpj5.html">FPJ-5</a> es el informe de una <strong>captura en flagrancia</strong>; el FPJ-4 es el formato de la <strong>actuación del primer responsable</strong>, con o sin capturados: tiene una sección para registrarlos (la 8), junto con las demás secciones del lugar de los hechos.</p>
<p>Lo que mostramos aquí corresponde a la <strong>Versión 04</strong> del formato (aprobada el 26 de julio de 2022 y publicada el 19 de agosto de 2022). Verifica siempre que uses el formato vigente en tu institución.</p>
<div class="tip"><p><strong>Víctimas:</strong> el FPJ-4 no tiene una sección de víctimas, a diferencia del FPJ-5. Las personas afectadas se registran como heridos o muertos.</p></div>'''),
        ('verificar', 'Antes de firmar, revisa esto', '''
<ul>
<li>El <strong>NUNC</strong> es el mismo en todos los documentos del caso.</li>
<li>Dejaste constancia del <strong>acordonamiento</strong> (o de por qué no) y de si hubo <strong>alteración</strong>.</li>
<li>Registraste a todos los <strong>intervinientes</strong> y todo <strong>EMP recibido</strong>, con hora y persona.</li>
<li>La <strong>cantidad</strong> de heridos, muertos y capturados corresponde a lo que relacionaste; lo que no cabe va al anexo.</li>
<li>Las <strong>fechas y horas</strong> (hechos, relevo y recibido) son coherentes entre sí.</li>
<li>Si hubo captura, los datos del capturado coinciden con el <a href="informe-captura-flagrancia-fpj5.html">FPJ-5</a> y el <a href="acta-derechos-capturado-fpj6.html">acta de derechos</a>.</li></ul>'''),
        ('app', 'También puedes diligenciarlo con la aplicación', '''
<div class="tip"><p>CapturaDocs Express también incluye el proceso de <strong>primer respondiente</strong>: sigue el orden del formato, reutiliza datos que ya escribiste (direcciones y personas) y genera el FPJ-4 con el formato oficial, además de los rótulos y la cadena de custodia de los elementos. Es un servicio adicional; <a href="../guia.html">aquí está cómo funciona</a>.</p></div>'''),
    ],
    faq=[
        ('¿Qué diferencia hay entre el FPJ-4 y el FPJ-5?', 'El FPJ-4 es la actuación del primer responsable en el lugar de los hechos: tiene una sección para personas capturadas (SI o NO), pero también pregunta por protección del lugar, heridos, muertos y relevo. El FPJ-5 es el informe de una captura en flagrancia. Son formatos distintos.'),
        ('¿Quién diligencia el FPJ-4?', 'El primer responsable: la sección 10 pide sus nombres, identificación, entidad, cargo, celular, CAI o estación, cuadrante y firma. Si es relevado, el formato tiene espacio para registrar el relevo, y la sección 11 es la constancia de quien recibe el lugar.'),
        ('¿Hay una sección de víctimas en el FPJ-4?', 'No. A diferencia del FPJ-5, este formato no pregunta por víctimas: las personas afectadas se registran como heridos o muertos, según el caso.'),
        ('¿Qué hago si hay más de un herido, muerto, vehículo o testigo?', 'El formato tiene espacio para uno de cada uno. Los demás se relacionan en el anexo de la actuación del primer responsable.'),
        ('¿Qué pasa con el FPJ-4 si hubo una captura?', 'La sección 8 del FPJ-4 registra a las personas capturadas. Los formatos propios de la captura (FPJ-5 y FPJ-6) son otros documentos. Confirma con tu superior o tu fiscal cuáles corresponden a tu actuación.'),
        ('¿La aplicación ayuda a diligenciar el FPJ-4?', 'Sí. CapturaDocs Express tiene un proceso de primer respondiente que sigue el orden del formato y genera el FPJ-4, además de los rótulos y la cadena de custodia. Puedes probarlo gratis.'),
    ],
    rel=['informe-captura-flagrancia-fpj5', 'rotulo-elementos-fpj7', 'captura-en-flagrancia-colombia'],
    fuentes=['Formato FPJ-4 (Actuación del Primer Responsable), versión 04, aprobación 2022-07-26 (Consejo Nacional de Policía Judicial), publicación 2022-08-19: contenido de las secciones tomado del propio formato.'],
)
PAGINAS = [FPJ4]
