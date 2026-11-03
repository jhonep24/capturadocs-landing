# Centro de ayuda: una guía por formato (FPJ-5, FPJ-6, FPJ-7, FPJ-8).
# Los datos de cada casilla salen de los formatos mismos (impresos en nuestras muestras) y de los artículos de la Ley 906 de 2004.
from c_flagrancia import LEY, LEY6

FPJ5 = dict(
    slug='informe-captura-flagrancia-fpj5', grupo='formatos', corto='Informe de Captura (FPJ-5)', icono='clipboard-list',
    titulo='Cómo diligenciar el Informe de Captura en Flagrancia FPJ-5',
    desc='Guía casilla por casilla del FPJ-5: NUNC, destino, conducta punible, datos del capturado, víctimas, testigos, elementos, narración de los hechos y firma.',
    desc_card='Las 11 secciones del informe, casilla por casilla.',
    kicker='Formato FPJ-5', min=9,
    h1='Informe de Captura en Flagrancia FPJ-5: <em>cómo diligenciarlo bien</em>',
    h1_plano='Informe de Captura en Flagrancia FPJ-5: cómo diligenciarlo bien',
    lead='El FPJ-5 es el informe que acompaña la captura: cuenta quién fue capturado, dónde, por qué y con qué elementos. Aquí está lo que va en cada una de sus 11 secciones y cómo evitar que lo devuelvan.',
    secciones=[
        ('que-es', '¿Qué es el FPJ-5 y quién lo diligencia?', '''
<p>El <strong>Informe de Captura en Flagrancia (FPJ-5)</strong> es el documento en el que el servidor de policía que hizo la captura deja constancia de las circunstancias. El mismo formato lo dice en su encabezado: «Este formato será diligenciado por Policía Nacional o Judicial en casos de captura». Es el «informe detallado» que menciona el artículo 302 del Código de Procedimiento Penal, y es lo que la Fiscalía usa para decidir cómo presentar al aprehendido ante el juez.</p>
<p>La versión que mostramos en estas guías es la <strong>Versión 04</strong> (aprobada el 28 de agosto de 2019 y publicada el 3 de septiembre de 2019), que tiene <strong>tres hojas</strong>. Revisa siempre que el formato que uses sea el vigente en tu institución.</p>'''),
        ('encabezado', 'El encabezado: NUNC, ciudad y fecha', '''
<figure class="doc"><img src="../img/ayuda-fpj5-encabezado.jpg" alt="Primera hoja del FPJ-5 con el Número Único de Noticia Criminal, el destino del informe, la conducta punible, el lugar de los hechos y los datos del capturado" width="940" height="760" loading="lazy"/><figcaption>Primera hoja del FPJ-5 con datos de ejemplo inventados.</figcaption></figure>
<ul>
<li><strong>Número Único de Noticia Criminal (NUNC):</strong> se escribe un dígito por casilla, siguiendo las divisiones impresas: Departamento, Municipio, Entidad, Unidad receptora, Año y Consecutivo. Es el número que identifica el caso en la Fiscalía y es <strong>el mismo en los cuatro formatos</strong>.</li>
<li><strong>Radicado interno:</strong> casilla para el número de radicado de tu unidad.</li>
<li><strong>Departamento, municipio y fecha:</strong> los del lugar de los hechos, con la fecha en año, mes y día.</li></ul>
<div class="tip"><p><strong>Consejo:</strong> copia el NUNC de una sola fuente y no lo retipees en cada formato. Un dígito cambiado es suficiente para que los documentos no «hablen» del mismo caso.</p></div>'''),
        ('secciones', 'Las 11 secciones, una por una', '''
<div class="tabla"><table><thead><tr><th>Sección</th><th>Qué va ahí</th></tr></thead><tbody>
<tr><td>1. Destino del informe</td><td>A quién se dirige: el fiscal o la unidad receptora (por ejemplo, la URI de tu ciudad).</td></tr>
<tr><td>2. Presunta conducta punible</td><td>El delito que se atribuye, con el artículo del Código Penal. Hay espacio para varios.</td></tr>
<tr><td>3. Lugar de los hechos</td><td>Dirección, barrio, localidad, departamento y municipio; si aplica, zona, vereda y características del sitio.</td></tr>
<tr><td>4. Información del capturado</td><td>Nombres y apellidos completos, alias, documento (tipo, número y lugar de expedición), edad, género, fecha y lugar de nacimiento, estado civil, escolaridad, ocupación, correo y redes, señales particulares y nombres de los padres.</td></tr>
<tr><td>5. Víctimas</td><td>Los mismos datos personales de cada víctima y su relación con el indiciado. Si no hay víctima identificada, se deja en blanco.</td></tr>
<tr><td>6. Testigos de los hechos</td><td>Los mismos datos de cada testigo y su contacto.</td></tr>
<tr><td>7. Descripción de EMP y EF recolectados</td><td>Cada elemento material probatorio o evidencia física, con el sitio de remisión bajo cadena de custodia.</td></tr>
<tr><td>8. Vehículos implicados</td><td>Marca, clase, color, propietario y placas.</td></tr>
<tr><td>9. Narración de los hechos</td><td>El relato en forma cronológica y concreta, más la fecha y hora de la captura y la fecha y hora en que se pone a disposición del fiscal.</td></tr>
<tr><td>10. Anexos</td><td>Los documentos que acompañan: acta de derechos, cadena de custodia, rótulos y lo demás que anexes.</td></tr>
<tr><td>11. Servidor que efectúa la captura</td><td>Nombres y apellidos, identificación, entidad, cargo, teléfono, correo y firma.</td></tr></tbody></table></div>
<p>El formato aclara que <strong>si hay más capturados, víctimas o testigos, las casillas se pueden reproducir cuantas veces sea necesario</strong>, y que si se necesita más espacio para describir los elementos o narrar, se pueden ampliar las filas.</p>
<figure class="doc"><img src="../img/ayuda-fpj5-hoja2.jpg" alt="Segunda hoja del FPJ-5 con víctimas, testigos, descripción de elementos recolectados y vehículos implicados" width="940" height="1140" loading="lazy"/><figcaption>Segunda hoja: víctimas, testigos, elementos recolectados y vehículos.</figcaption></figure>'''),
        ('narracion', 'La narración de los hechos', '''
<figure class="doc"><img src="../img/ayuda-fpj5-hoja3.jpg" alt="Tercera hoja del FPJ-5 con la narración de los hechos, los anexos y el servidor que efectúa la captura" width="940" height="585" loading="lazy"/><figcaption>Tercera hoja: narración, anexos y datos de quien hace la captura.</figcaption></figure>
<p>El título de la sección lo resume: <strong>«en forma cronológica y concreta»</strong>. Una narración útil responde, en orden, a qué, quién, cuándo, dónde y cómo:</p>
<ol class="lista">
<li><strong>Cuándo y dónde:</strong> fecha, hora y sitio exacto en que se produjo la captura.</li>
<li><strong>Qué se observó:</strong> lo que vio el uniformado, o lo que le informó la víctima o un testigo, y cómo se individualizó a la persona.</li>
<li><strong>Cómo fue la aprehensión:</strong> si hubo persecución, si se señaló a la persona, qué elementos tenía consigo.</li>
<li><strong>Derechos:</strong> que se le informaron sus derechos de manera inmediata (art. 303).</li>
<li><strong>Elementos:</strong> qué se incautó, dónde, quién lo embaló y lo rotuló.</li>
<li><strong>Traslado:</strong> a dónde se condujo al capturado y a qué hora se puso a disposición del fiscal.</li></ol>
<div class="alerta"><p><strong>Evita:</strong> opiniones («un sujeto de mala catadura»), adjetivos sin hecho y datos que no coinciden con los demás formatos. Cuenta lo que pasó, no lo que concluyes. Tenemos una <a href="como-redactar-la-narracion-de-los-hechos.html">guía completa para redactar la narración</a>.</p></div>'''),
        ('verificar', 'Antes de firmar, revisa esto', '''
<ul>
<li>El <strong>NUNC</strong> es el mismo en el FPJ-5, el FPJ-6, el FPJ-7 y el FPJ-8.</li>
<li>La <strong>fecha y hora de la captura</strong> coinciden con las del acta de derechos. El propio formato lo advierte debajo de ese campo.</li>
<li>El <strong>nombre y el documento</strong> del capturado están escritos igual en todos los documentos.</li>
<li>La <strong>descripción de los elementos</strong> es igual en el FPJ-5, en el rótulo y en la cadena de custodia.</li>
<li>Pusiste el <strong>delito con su artículo</strong> y el <strong>destino</strong> del informe.</li>
<li>Marcaste los <strong>anexos</strong> que realmente adjuntas y revisaste la firma.</li></ul>
<p>Más detalles en <a href="errores-comunes-informes-captura.html">los errores más comunes</a> y en la <a href="lista-de-chequeo-captura-flagrancia.html">lista de chequeo imprimible</a>.</p>'''),
    ],
    faq=[
        ('¿Cuántas hojas tiene el FPJ-5?', 'La versión 04 del formato tiene tres hojas: datos del encabezado, lugar y capturado en la primera; víctimas, testigos, elementos y vehículos en la segunda; narración, anexos y servidor que captura en la tercera.'),
        ('¿Qué significa EMP y EF en el informe?', 'EMP son los elementos materiales probatorios y EF la evidencia física: los objetos, huellas o rastros que se recogen en el procedimiento y que se describen en la sección 7 del informe y en los formatos de rótulo y cadena de custodia.'),
        ('¿Qué hago si hay más de un capturado?', 'El formato indica que, si existen más capturados, se pueden reproducir las casillas del capturado cuantas veces sea necesario. Lo mismo vale para víctimas y testigos.'),
        ('¿Debo llenar víctimas y testigos aunque no existan?', 'Si no hay víctima o testigo identificado, esas secciones se dejan sin datos. Lo importante es que lo que sí escribas coincida con los demás documentos y con la narración.'),
        ('¿Puedo generar el FPJ-5 automáticamente?', 'Sí. CapturaDocs Express llena el FPJ-5 junto con el FPJ-6, el FPJ-7, el FPJ-8 y el acta de incautación a partir de un solo formulario, con el formato oficial. Puedes probarlo gratis con 5 casos.'),
    ],
    rel=['acta-derechos-capturado-fpj6', 'como-redactar-la-narracion-de-los-hechos', 'errores-comunes-informes-captura'],
    fuentes=['Formato FPJ-5, versión 04, aprobada el 28 de agosto de 2019 (CPJ).', 'Ley 906 de 2004, art. 302: ' + LEY + '.'],
)

FPJ6 = dict(
    slug='acta-derechos-capturado-fpj6', grupo='formatos', corto='Acta de Derechos (FPJ-6)', icono='file-pen',
    titulo='Acta de Derechos del Capturado FPJ-6: cómo diligenciarla',
    desc='Qué es el FPJ-6, qué derechos se informan según el art. 303 del C.P.P., cómo llenar los datos personales, la constancia de buen trato y las firmas.',
    desc_card='Los derechos del art. 303 y los datos personales del capturado.',
    kicker='Formato FPJ-6', min=7,
    h1='Acta de Derechos del Capturado FPJ-6: <em>cómo diligenciarla</em>',
    h1_plano='Acta de Derechos del Capturado FPJ-6: cómo diligenciarla',
    lead='El FPJ-6 deja por escrito que al capturado se le informaron sus derechos y recoge sus datos personales. Aquí está qué dice el artículo 303 y cómo llenar cada parte del acta.',
    secciones=[
        ('que-es', '¿Qué es el FPJ-6?', '''
<p>El <strong>Acta de Derechos del Capturado (FPJ-6)</strong> es el formato en el que se deja constancia de que, al momento de la captura, se le hizo saber al capturado el contenido del <strong>artículo 303 del Código de Procedimiento Penal</strong>. Su encabezado indica que lo diligencia la Policía Nacional o Judicial en casos de captura. La versión que mostramos es la <strong>Versión 03</strong> (aprobada el 26 de julio de 2022), de <strong>dos hojas</strong>.</p>
<p>Se llena <strong>un acta por cada capturado</strong>.</p>'''),
        ('derechos', 'Los cuatro derechos que se informan (art. 303)', '''
<figure class="doc"><img src="../img/ayuda-fpj6-derechos.jpg" alt="Texto del Acta de Derechos del Capturado FPJ-6 con los cuatro derechos del artículo 303" width="940" height="295" loading="lazy"/><figcaption>El texto de los derechos ya viene impreso en el formato.</figcaption></figure>
<div class="norma"><h3>Al capturado se le informa de manera inmediata</h3><ol>
<li>El hecho que se le atribuye y motivó su captura, y el funcionario que la ordenó.</li>
<li>Su derecho a indicar la persona a quien se deba comunicar su aprehensión.</li>
<li>Su derecho a guardar silencio, que lo que diga podrá usarse en su contra y que no está obligado a declarar contra su cónyuge, compañero permanente o parientes dentro del cuarto grado de consanguinidad o civil, o segundo de afinidad.</li>
<li>Su derecho a designar y entrevistarse con un abogado de confianza en el menor tiempo posible; si no puede, la defensa la provee el Sistema Nacional de Defensoría Pública.</li></ol></div>
<p>La palabra clave del artículo es <strong>«inmediata»</strong>. Por eso la hora que escribes en el acta debe corresponder al momento real de la lectura de derechos y coincidir con la del informe FPJ-5.</p>'''),
        ('datos', 'Los datos personales del capturado', '''
<p>Después de los derechos, el acta dice «una vez enterada de sus derechos, manifestó» y pide los datos personales. Se escriben tal como los entrega la persona y se verifican con su documento:</p>
<ul>
<li><strong>Nombre identitario</strong> (solo para personas trans): el nombre con el que la persona se identifica, independiente de su nombre legal; así lo aclara el pie de página del formato.</li>
<li><strong>Nombres y apellidos e identificación</strong>, con el tipo y número de documento y el lugar de expedición.</li>
<li><strong>Fecha y lugar de nacimiento</strong>, nombres de los padres, estado civil y ocupación u oficio.</li>
<li><strong>Dirección y teléfono, correo electrónico y redes sociales.</strong></li>
<li><strong>Autoidentificación:</strong> si se identifica como persona LGBTI y su pertenencia étnica (indígena, negro/a, raizal, afrocolombiano, palenquero/a, rrom) y la comunidad. Son datos de autoidentificación: se pregunta con respeto y se escribe lo que la persona responda.</li></ul>
<div class="tip"><p><strong>Cuidado con la fecha de nacimiento:</strong> es el dato que más se deja en blanco o se escribe distinto al de otros formatos. En el FPJ-5 se pide la edad y la fecha de nacimiento por casillas; en el FPJ-6 y en la constancia de buen trato se repite. Escríbelo igual en los tres lugares.</p></div>'''),
        ('segunda-hoja', 'La segunda hoja: comunicación, firmas y buen trato', '''
<ol class="lista">
<li><strong>Que ha entendido los derechos leídos.</strong> La persona lo manifiesta.</li>
<li><strong>La persona a quien desea que se comunique su captura:</strong> nombres y apellidos, identificación, teléfono y hora en que se hizo la comunicación (es el derecho número 2 del artículo 303).</li>
<li><strong>Observaciones</strong>, si las hay.</li>
<li><strong>Firma y huella del capturado</strong> y <strong>nombre, cédula y firma del servidor</strong>.</li>
<li><strong>Constancia de buen trato:</strong> declaración de que la persona recibió buen trato físico, psicológico y moral y de que se le comunicaron y respetaron sus derechos. Lleva ciudad, día, mes, año, hora, datos del capturado, el delito y las firmas del capturado y del fiscal.</li></ol>
<div class="alerta"><p>La constancia de buen trato <strong>repite datos</strong> del acta (nombre, documento, edad, estado civil, delito). Si el nombre o el delito no coinciden con los del FPJ-5, el problema salta a la vista.</p></div>'''),
        ('consejos', 'Consejos para que el acta quede limpia', '''
<ul>
<li>Lee los derechos <strong>en voz alta y completos</strong> y llena el acta en ese momento o apenas sea posible.</li>
<li>Pregunta el nombre y escríbelo exactamente como aparece en el documento.</li>
<li>Si la persona no quiere firmar, deja la anotación en observaciones en lugar de dejar el espacio sin explicación.</li>
<li>Usa la misma <strong>ciudad, fecha y hora</strong> que en el FPJ-5.</li></ul>
<p>Si quieres ver cómo se conecta con el resto de los documentos, mira <a href="captura-en-flagrancia-colombia.html">la guía de captura en flagrancia</a>.</p>'''),
    ],
    faq=[
        ('¿Cuántos derechos se le informan al capturado?', 'El artículo 303 del Código de Procedimiento Penal enumera cuatro: conocer el hecho que se le atribuye, indicar a quién se comunica su captura, guardar silencio sin que se use en su contra y designar abogado de confianza o contar con defensor público.'),
        ('¿Se hace un acta por cada capturado?', 'Sí. El FPJ-6 es individual: cada persona capturada tiene su propia acta con sus datos y sus firmas.'),
        ('¿Qué es la constancia de buen trato?', 'Es la declaración al final del acta en la que el capturado manifiesta que recibió buen trato físico, psicológico y moral y que se le comunicaron y respetaron sus derechos. Va firmada por el capturado y por el fiscal.'),
        ('¿El nombre identitario es obligatorio?', 'Es una casilla pensada para personas trans: es el nombre con el que se auto identifican, independiente de su nombre legal. Se llena solo cuando corresponde.'),
        ('¿Puedo generar el FPJ-6 automáticamente?', 'Sí. CapturaDocs Express llena el acta con los mismos datos del informe, para que el nombre, el documento y la fecha no cambien entre documentos. Pruébalo gratis con 5 casos.'),
    ],
    rel=['informe-captura-flagrancia-fpj5', 'captura-en-flagrancia-colombia', 'errores-comunes-informes-captura'],
    fuentes=['Formato FPJ-6, versión 03, aprobada el 26 de julio de 2022 (CNPJ).', 'Ley 906 de 2004, art. 303: ' + LEY + '.'],
)

FPJ7 = dict(
    slug='rotulo-elementos-fpj7', grupo='formatos', corto='Rótulo de elementos (FPJ-7)', icono='target',
    titulo='Rótulo de elementos materiales probatorios FPJ-7: cómo llenarlo',
    desc='Cómo diligenciar el rótulo FPJ-7: NUNC, fecha y hora de recolección, hallazgo, sitio, persona a quien se halló, descripción del elemento y quién lo diligenció.',
    desc_card='Un rótulo por cada elemento incautado, casilla por casilla.',
    kicker='Formato FPJ-7', min=6,
    h1='Rótulo FPJ-7 de elementos materiales probatorios: <em>cómo llenarlo</em>',
    h1_plano='Rótulo FPJ-7 de elementos materiales probatorios: cómo llenarlo',
    lead='El rótulo identifica cada elemento que se recoge en la captura. Se llena uno por elemento y se pega al embalaje. Estas son sus siete casillas y lo que conviene escribir en cada una.',
    secciones=[
        ('que-es', '¿Qué es el rótulo FPJ-7?', '''
<p>El <strong>Rótulo de Elementos Materiales Probatorios y Evidencia Física (FPJ-7)</strong> es la «etiqueta» que se asigna a cada elemento recolectado en el lugar de los hechos o en la captura. Junto con el <a href="cadena-de-custodia-fpj8.html">Registro de Cadena de Custodia (FPJ-8)</a> permite saber de qué elemento se trata, dónde se halló, quién lo halló y quién lo ha tenido.</p>
<p>La versión que mostramos es la <strong>Versión 04</strong> (aprobada el 18 de abril de 2018), en <strong>una sola hoja horizontal</strong>. El formato de cadena de custodia advierte que los formatos FPJ-7 y FPJ-8 son <strong>exclusivos para la función de Policía Judicial</strong>.</p>
<p>Se llena <strong>un rótulo por cada elemento</strong>. Si incautaste un celular y una billetera, son dos rótulos.</p>'''),
        ('casillas', 'Las siete casillas', '''
<figure class="doc"><img src="../img/doc-fpj7.jpg" alt="Rótulo FPJ-7 diligenciado con datos de ejemplo inventados" width="1400" height="866" loading="lazy"/><figcaption>Rótulo FPJ-7 con datos de ejemplo inventados.</figcaption></figure>
<div class="tabla"><table><thead><tr><th>Casilla</th><th>Qué va ahí</th></tr></thead><tbody>
<tr><td>1. NUNC</td><td>El Número Único de Noticia Criminal, igual que en los demás formatos.</td></tr>
<tr><td>2. No. ID</td><td>Casilla de identificación del rótulo; el instructivo oficial vigente indica cómo asignarla.</td></tr>
<tr><td>3. Fecha y hora de recolección</td><td>Año, mes y día en casillas separadas (por ejemplo 2026 10 28) y la hora en formato de 24 horas (14:30 se escribe 1430).</td></tr>
<tr><td>4. Hallazgo</td><td>El número del elemento (01, 02…) y la cantidad. Es el número de orden dentro del caso.</td></tr>
<tr><td>5. Sitio o lugar de hallazgo</td><td>La dirección donde se encontró y la <strong>ubicación específica</strong> (por ejemplo, «bolsillo derecho del pantalón») y, a la derecha, nombre y documento de la persona a quien se le encontró el elemento.</td></tr>
<tr><td>6. Descripción del elemento</td><td>Qué es, con los datos que lo distinguen de otro igual.</td></tr>
<tr><td>7. Rótulo diligenciado por</td><td>Nombres y apellidos, cédula, entidad, cargo y firma de quien lo llena.</td></tr></tbody></table></div>'''),
        ('descripcion', 'Cómo describir bien un elemento', '''
<p>La descripción (casilla 6) es la parte más importante y la que más veces queda corta. Su objetivo es que alguien que nunca vio el elemento lo pueda reconocer. Incluye, según el caso:</p>
<ul>
<li><strong>Qué es:</strong> celular, arma, billetera, bolso, sustancia…</li>
<li><strong>Marca, modelo y color.</strong></li>
<li><strong>Identificadores:</strong> serial, IMEI, número de arma, placa.</li>
<li><strong>Estado:</strong> con o sin fisuras, con golpes, abierto o cerrado, cantidad de piezas.</li>
<li><strong>Cantidad</strong> y, si hay varios, su número de orden.</li></ul>
<div class="tip"><p><strong>Una regla simple:</strong> escribe la descripción una vez y <strong>cópiala igual</strong> al FPJ-5 (sección 7), al FPJ-8 (casilla 5) y al embalaje. Cuando la misma cosa aparece con tres descripciones distintas, aparece la duda sobre si es el mismo elemento.</p></div>
<h3>¿Y los objetos muy grandes?</h3>
<p>El artículo 256 de la Ley 906 trata los «macroelementos»: naves, aeronaves, vehículos, máquinas y objetos similares. Dice que, después de ser examinados por peritos, se graban en video o se fotografían en su totalidad y, en especial, los sitios donde se hallaron huellas o rastros; esas fotos y videos sustituyen al elemento físico y se embalan, rotulan y conservan en la forma prevista.</p>'''),
        ('legal', 'Por qué importa el rótulo', '''
<p>El artículo 254 del Código de Procedimiento Penal dice que la cadena de custodia se aplica «con el fin de demostrar la autenticidad» de los elementos materiales probatorios y evidencia física, teniendo en cuenta su <strong>identidad, estado original, condiciones de recolección, preservación, embalaje y envío</strong>, los lugares y fechas de permanencia y los cambios que cada custodio haya hecho. Y empieza «en el lugar donde se descubran, recauden o encuentren» los elementos.</p>
<p>El rótulo es la primera pieza de ese registro: fija <strong>qué</strong> se recogió, <strong>cuándo</strong>, <strong>dónde</strong> y <strong>a quién</strong> se le encontró.</p>'''),
    ],
    faq=[
        ('¿Se llena un rótulo por cada elemento?', 'Sí. Cada elemento material probatorio o evidencia física lleva su propio rótulo, con su número de orden y su descripción.'),
        ('¿Cómo se escribe la hora en el rótulo?', 'La hora se escribe en formato de 24 horas en casillas separadas, por ejemplo 14:30 como 1430. La fecha va en año, mes y día.'),
        ('¿Qué diferencia hay entre el FPJ-7 y el FPJ-8?', 'El FPJ-7 es el rótulo que identifica al elemento en el momento en que se recoge; el FPJ-8 es el registro de cadena de custodia que deja constancia de quién lo halló, lo recolectó y lo embaló, y de quienes lo reciben después.'),
        ('¿Quién diligencia el rótulo?', 'Quien recolecta el elemento. La casilla 7 pide sus nombres, cédula, entidad, cargo y firma.'),
        ('¿Puedo generar el rótulo automáticamente?', 'Sí. CapturaDocs Express genera el FPJ-7 con la descripción y los datos que ya escribiste en el caso, uno por cada elemento. También tiene una guía para imprimirlo en tamaño reducido y pegarlo al embalaje.'),
    ],
    rel=['cadena-de-custodia-fpj8', 'informe-captura-flagrancia-fpj5', 'lista-de-chequeo-captura-flagrancia'],
    fuentes=['Formato FPJ-7, versión 04, aprobada el 18 de abril de 2018 (CNPJ).', 'Ley 906 de 2004, arts. 254 y 256: ' + LEY6 + '.'],
)

FPJ8 = dict(
    slug='cadena-de-custodia-fpj8', grupo='formatos', corto='Cadena de Custodia (FPJ-8)', icono='lock-keyhole',
    titulo='Registro de Cadena de Custodia FPJ-8: cómo diligenciarlo',
    desc='Qué es el FPJ-8, qué significan las marcas H, R y E, quién firma, cómo se describe el elemento y qué dicen los arts. 254 a 259 de la Ley 906.',
    desc_card='Las marcas H, R y E, las firmas y los artículos 254 a 259.',
    kicker='Formato FPJ-8', min=7,
    h1='Registro de Cadena de Custodia FPJ-8: <em>cómo diligenciarlo</em>',
    h1_plano='Registro de Cadena de Custodia FPJ-8: cómo diligenciarlo',
    lead='El FPJ-8 es el historial del elemento: quién lo halló, quién lo recolectó, quién lo embaló y quién lo ha tenido después. Qué significan las marcas H, R y E y cómo evitar los errores típicos.',
    secciones=[
        ('que-es', '¿Qué es la cadena de custodia?', '''
<p>La cadena de custodia es el conjunto de pasos y registros que demuestran que un elemento material probatorio es el mismo que se recogió y que no fue alterado. El <strong>artículo 254</strong> del Código de Procedimiento Penal la aplica «con el fin de demostrar la autenticidad» de los elementos y evidencia física, teniendo en cuenta:</p>
<ul>
<li>su identidad y estado original,</li>
<li>las condiciones de recolección, preservación, embalaje y envío,</li>
<li>los lugares y fechas de permanencia y los cambios que cada custodio haya hecho,</li>
<li>y el nombre y la identificación de <strong>todas las personas que hayan estado en contacto</strong> con esos elementos.</li></ul>
<p>Empieza <strong>donde se descubren, recaudan o encuentran</strong> los elementos y termina por orden de autoridad competente. El <strong>artículo 255</strong> pone la responsabilidad de aplicarla en los servidores públicos que entren en contacto con ellos.</p>'''),
        ('formato', 'El formato FPJ-8 casilla por casilla', '''
<figure class="doc"><img src="../img/doc-fpj8.jpg" alt="Registro de cadena de custodia FPJ-8 diligenciado con datos de ejemplo inventados" width="1400" height="933" loading="lazy"/><figcaption>FPJ-8 con datos de ejemplo inventados.</figcaption></figure>
<div class="tabla"><table><thead><tr><th>Casilla</th><th>Qué va ahí</th></tr></thead><tbody>
<tr><td>1. NUNC</td><td>El Número Único de Noticia Criminal, idéntico al de los demás formatos.</td></tr>
<tr><td>2. No. ID</td><td>Casilla de identificación del registro; el instructivo oficial vigente indica cómo asignarla.</td></tr>
<tr><td>3. No. de historia clínica (*)</td><td>Solo lo diligencia la entidad prestadora de salud cuando es ella quien recolecta el elemento.</td></tr>
<tr><td>4. Documentación de los elementos</td><td>Una fila por cada persona que interviene: las marcas H, R y E, nombres y apellidos, cédula, entidad y firma con la fecha.</td></tr>
<tr><td>5. Descripción</td><td>La descripción del elemento, igual a la del rótulo y a la del informe.</td></tr></tbody></table></div>'''),
        ('hre', 'Las marcas H, R y E', '''
<p>Las convenciones del formato lo dicen: <strong>H, R, E</strong> significan que se marca con una X si la persona <strong>Halló, Recolectó o Embaló</strong> el elemento, respectivamente. Y se puede marcar <strong>una o varias opciones para un mismo nombre</strong>, según sea el caso.</p>
<div class="tabla"><table><thead><tr><th>Marca</th><th>Significa</th><th>Ejemplo</th></tr></thead><tbody>
<tr><td>H</td><td>Halló el elemento</td><td>Quien lo vio o lo encontró.</td></tr>
<tr><td>R</td><td>Recolectó el elemento</td><td>Quien lo tomó y lo retiró del sitio.</td></tr>
<tr><td>E</td><td>Embaló el elemento</td><td>Quien lo guardó en su empaque y lo selló.</td></tr></tbody></table></div>
<div class="tip"><p>Si la misma persona hizo las tres cosas, se marcan las tres casillas en su fila, como en el ejemplo de arriba. Si lo hicieron personas distintas, cada una lleva su propia fila.</p></div>'''),
        ('legal', 'Lo que dice la ley sobre el recorrido del elemento', '''
<ol class="lista">
<li><strong>Art. 257 — Inicio:</strong> el servidor público que, en la actuación de indagación o investigación policial, hubiere embalado y rotulado el elemento, lo custodiará.</li>
<li><strong>Art. 258 — Traslado:</strong> el funcionario de policía judicial o servidor que recogió, embaló y rotuló lo traslada al laboratorio correspondiente y lo entrega en la oficina de correspondencia, <strong>bajo el recibo que figura en el formato de cadena de custodia</strong>.</li>
<li><strong>Art. 259 — Traspaso:</strong> quien recibe en correspondencia, sin pérdida de tiempo y bajo el recibo del mismo formato, entrega el contenedor al perito que corresponda según su especialidad.</li></ol>
<p>Por eso cada persona que recibe o entrega el elemento firma y fecha en el FPJ-8: es la forma de que nunca quede un tramo sin responsable.</p>'''),
        ('errores', 'Los errores que más se repiten', '''
<ul>
<li>Marcar H, R o E sin que la persona haya hecho esa tarea, o dejar una persona que sí intervino sin su fila.</li>
<li>Firmas sin fecha, o con una fecha anterior a la de recolección del rótulo.</li>
<li>Descripción distinta a la del rótulo o a la del informe.</li>
<li>Nombre o cédula escritos distinto al resto de documentos del caso.</li>
<li>Llenar «historia clínica» cuando no corresponde: es solo para la entidad de salud.</li></ul>
<p>La <a href="lista-de-chequeo-captura-flagrancia.html">lista de chequeo imprimible</a> los recoge todos.</p>'''),
    ],
    faq=[
        ('¿Qué significan H, R y E en el FPJ-8?', 'Se marca con una X si la persona Halló, Recolectó o Embaló el elemento. Se pueden marcar una o varias opciones para un mismo nombre.'),
        ('¿Qué es el número de historia clínica del formato?', 'Es una casilla marcada con asterisco que solo diligencia la entidad prestadora de salud cuando es ella quien recolecta el elemento material probatorio o la evidencia física.'),
        ('¿Quién firma el registro de cadena de custodia?', 'Cada persona que interviene con el elemento tiene su fila con nombre, cédula, entidad y firma con fecha. Así queda registro de todas las personas que estuvieron en contacto con él (art. 254).'),
        ('¿Cuándo empieza y cuándo termina la cadena de custodia?', 'Empieza en el lugar donde se descubren, recaudan o encuentran los elementos y finaliza por orden de autoridad competente, según el artículo 254 del Código de Procedimiento Penal.'),
        ('¿Puedo generar el FPJ-8 automáticamente?', 'Sí. CapturaDocs Express genera el FPJ-8 con las marcas H, R y E y los datos de quienes intervinieron, a partir del mismo formulario del caso.'),
    ],
    rel=['rotulo-elementos-fpj7', 'informe-captura-flagrancia-fpj5', 'errores-comunes-informes-captura'],
    fuentes=['Formato FPJ-8 (convenciones impresas en el mismo formato).', 'Ley 906 de 2004, arts. 254 a 259: ' + LEY6 + '.'],
)
PAGINAS = [FPJ5, FPJ6, FPJ7, FPJ8]
