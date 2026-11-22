# Centro de ayuda: portada y página de captura en flagrancia.
# Los artículos citados salen del texto de la Ley 906 de 2004 publicado por la Secretaría del Senado (consultado el 2026-10-30).
LEY = '<a href="http://www.secretariasenado.gov.co/senado/basedoc/ley_0906_2004_pr007.html" rel="noopener">Ley 906 de 2004 (Código de Procedimiento Penal), Secretaría del Senado</a>'
LEY6 = '<a href="http://www.secretariasenado.gov.co/senado/basedoc/ley_0906_2004_pr006.html" rel="noopener">Ley 906 de 2004, arts. 245 a 286, Secretaría del Senado</a>'

INDEX = dict(
    slug='index', grupo='hub', corto='Centro de ayuda', icono='life-buoy',
    titulo='Ayuda para informes de captura en flagrancia (FPJ-5, 6, 7 y 8) | CapturaDocs Express',
    desc='Guías claras para diligenciar el Informe de Captura FPJ-5, el Acta de Derechos FPJ-6, el Rótulo FPJ-7 y la Cadena de Custodia FPJ-8, con la norma citada.',
    desc_card='Todas las guías en un solo lugar.',
    kicker='Centro de ayuda',
    h1='Informes de captura en flagrancia, <em>sin dudas.</em>',
    h1_plano='Informes de captura en flagrancia, sin dudas',
    lead='Guías prácticas para diligenciar cada formato FPJ de la Policía Judicial: qué va en cada casilla, qué dice la norma y dónde se equivocan más los informes. Hechas para el uniformado que tiene que dejarlo bien a la primera.',
    min=3, secciones=[], faq=[
        ('¿Qué son los formatos FPJ de una captura en flagrancia?',
         'Son los formatos estandarizados de la Policía Judicial que se diligencian en una captura: el Informe de Captura en Flagrancia (FPJ-5), el Acta de Derechos del Capturado (FPJ-6), el Rótulo de elementos materiales probatorios (FPJ-7) y el Registro de Cadena de Custodia (FPJ-8).'),
        ('¿Estas guías reemplazan el instructivo oficial?',
         'No. Son una ayuda de lectura en lenguaje sencillo. Para cualquier duda sobre el diligenciamiento, manda el instructivo oficial vigente y la orientación de tu fiscal o de tu superior.'),
        ('¿CapturaDocs Express es una aplicación oficial?',
         'No. Es una herramienta privada e independiente que ayuda a llenar los formatos una sola vez y generarlos todos. No está afiliada ni avalada por la Policía Nacional.'),
    ])

FLAGRANCIA = dict(
    slug='captura-en-flagrancia-colombia', grupo='practica', corto='Captura en flagrancia', icono='shield-check',
    titulo='Captura en flagrancia en Colombia: qué es y qué hacer paso a paso',
    desc='Qué es la flagrancia según el art. 301 del C.P.P., quién puede capturar, qué derechos se leen, el plazo de 36 horas y qué documentos se diligencian.',
    desc_card='Qué es la flagrancia, las 36 horas y los documentos del procedimiento.',
    kicker='Procedimiento', min=8, actualizado='22 de noviembre de 2026', modificado='2026-11-22',
    h1='Captura en flagrancia en Colombia: <em>qué es y qué hacer paso a paso</em>',
    h1_plano='Captura en flagrancia en Colombia: qué es y qué hacer paso a paso',
    lead='Cuándo hay flagrancia, quién puede capturar, qué se le informa al capturado y qué documentos se diligencian, explicado con lo que dice la Ley 906 de 2004.',
    secciones=[
        ('esencial', 'Lo esencial en 30 segundos', '''
<div class="tip"><p><strong>Resumen:</strong> hay flagrancia cuando la persona es sorprendida cometiendo el delito o aprehendida inmediatamente después (art. 301). Cualquiera puede capturar (art. 302). Al capturado se le informan sus derechos <strong>de inmediato</strong> (art. 303), se le identifica y registra, y la Fiscalía lo presenta al juez de control de garantías <strong>inmediatamente o, a más tardar, en 36 horas</strong>. En el papel, todo queda en cuatro formatos que deben contar la misma historia: FPJ-5, FPJ-6, FPJ-7 y FPJ-8.</p></div>
<ul>
<li><strong>Qué la define:</strong> la inmediatez entre el hecho y la captura.</li>
<li><strong>Qué se hace al instante:</strong> informar los derechos, identificar y registrar al aprehendido.</li>
<li><strong>Qué se documenta:</strong> informe, acta de derechos, rótulo de cada elemento y cadena de custodia.</li>
<li><strong>Cuánto hay:</strong> 36 horas como máximo para presentarlo ante el juez.</li></ul>'''),
        ('que-es', '¿Qué es la flagrancia?', '''
<p>La flagrancia es la situación en la que una persona es descubierta cometiendo un delito o justo después de cometerlo. El artículo 301 del Código de Procedimiento Penal (Ley 906 de 2004, modificado por la Ley 1453 de 2011) dice que hay flagrancia cuando:</p>
<div class="norma"><h3>Artículo 301 — cinco situaciones</h3><ol>
<li>La persona es sorprendida y aprehendida <strong>durante la comisión del delito</strong>.</li>
<li>La persona es sorprendida o individualizada durante la comisión del delito y aprehendida <strong>inmediatamente después, por persecución</strong>, o cuando la víctima u otra persona la señala como autora o cómplice inmediatamente después del hecho.</li>
<li>La persona es sorprendida y capturada <strong>con objetos, instrumentos o huellas</strong> de los que aparezca fundadamente que acaba de cometer un delito o de haber participado en él.</li>
<li>La persona es sorprendida o individualizada en la comisión del delito <strong>en un sitio abierto al público a través de la grabación de un dispositivo de video</strong> y aprehendida inmediatamente después. La misma regla aplica si la grabación se hace en un lugar privado con consentimiento de quienes residen allí.</li>
<li>La persona se encuentra <strong>en un vehículo utilizado momentos antes para huir</strong> del lugar del delito, salvo que aparezca fundadamente que no sabía de la conducta punible.</li></ol></div>
<p>Lo que une a las cinco es la <strong>inmediatez</strong>: la captura ocurre mientras se comete el hecho o enseguida. Si pasó mucho tiempo, ya no es flagrancia y se necesita otra vía legal.</p>'''),
        ('quien-captura', '¿Quién puede capturar en flagrancia?', '''
<p>El artículo 302 es claro: <strong>cualquier persona</strong> puede capturar a quien sea sorprendido en flagrancia. Lo que cambia es lo que hay que hacer después:</p>
<ul>
<li><strong>Si captura una autoridad:</strong> debe conducir al aprehendido inmediatamente, o a más tardar en el término de la distancia, ante la Fiscalía General de la Nación.</li>
<li><strong>Si captura un particular:</strong> debe llevarlo, en el término de la distancia, ante cualquier autoridad de policía. Esta identifica al aprehendido, recibe un informe detallado de las circunstancias de la captura y lo pone a disposición de la Fiscalía dentro del mismo plazo.</li></ul>
<p>Cuando captura un uniformado, el informe de la captura se deja en el <a href="informe-captura-flagrancia-fpj5.html">Informe de Captura en Flagrancia (FPJ-5)</a>: es el formato que se diligencia, según su propio encabezado, «por Policía Nacional o Judicial en casos de captura».</p>'''),
        ('derechos', 'Los derechos del capturado: se informan de manera inmediata', '''
<p>El artículo 303 obliga a informar al capturado <strong>de manera inmediata</strong>:</p>
<div class="norma"><h3>Artículo 303 — derechos del capturado</h3><ol>
<li>Del hecho que se le atribuye y motivó su captura, y el funcionario que la ordenó.</li>
<li>Del derecho a indicar la persona a quien se deba comunicar su aprehensión. El funcionario responsable del capturado procede de inmediato a comunicarlo.</li>
<li>Del derecho a guardar silencio, de que lo que diga podrá usarse en su contra y de que no está obligado a declarar contra su cónyuge, compañero permanente o parientes dentro del cuarto grado de consanguinidad o civil, o segundo de afinidad.</li>
<li>Del derecho a designar y entrevistarse con un abogado de confianza en el menor tiempo posible; si no puede, el Sistema Nacional de Defensoría Pública le proveerá su defensa.</li></ol></div>
<p>Esa información queda por escrito en el <a href="acta-derechos-capturado-fpj6.html">Acta de Derechos del Capturado (FPJ-6)</a>.</p>'''),
        ('identificar', 'Identificación y registro del aprehendido', '''
<p>El parágrafo del artículo 302 (agregado por la Ley 1142 de 2007) ordena que, <strong>en todos los casos de captura</strong>, la policía judicial proceda de inmediato a la <strong>plena identificación y registro</strong> del aprehendido, según el artículo 128 del Código, con el fin de constatar capturas anteriores, procesos en curso y antecedentes.</p>
<p>Por eso los datos personales del capturado (nombres, documento, lugar de nacimiento, padres, estado civil, dirección) tienen que quedar <strong>idénticos</strong> en todos los documentos. Un nombre escrito de dos maneras es el error más fácil de evitar y el que más molesta después. Lo explicamos en <a href="errores-comunes-informes-captura.html">los errores que conviene evitar</a>.</p>'''),
        ('treinta-y-seis', 'El plazo de las 36 horas', '''
<p>Según el artículo 302, la Fiscalía, con base en el informe de la autoridad (o del particular) y en los elementos materiales probatorios aportados, presenta al aprehendido <strong>inmediatamente o a más tardar dentro de las treinta y seis (36) horas siguientes</strong> ante el juez de control de garantías. Allí se revisa la legalidad de la aprehensión y se atienden las solicitudes de la Fiscalía, la defensa y el Ministerio Público.</p>
<div class="tip"><p><strong>Por qué importa para tu informe:</strong> los documentos son lo que la Fiscalía tiene en la mano para presentar el caso. Un informe completo y coherente al llegar ahorra idas y vueltas dentro de ese plazo. En el FPJ-5 hay un campo para la «fecha y hora en que es puesto a disposición del Fiscal»; la forma impresa advierte que los datos de fecha y hora de la captura deben coincidir con los del acta de derechos.</p></div>
<p>El mismo artículo trae una excepción (Ley 2111 de 2021) para capturas en zonas de difícil acceso, como ríos o sitios a los que solo se llega por vía fluvial: allí el plazo se cuenta desde la llegada al puerto o municipio más cercano y la autoridad debe acreditar la dificultad.</p>
<p>Y si de la información recogida aparece que el supuesto delito <strong>no comporta detención preventiva</strong>, o la captura fue ilegal, la Fiscalía libera al aprehendido imponiéndole, cuando sea necesario, un compromiso de comparecencia bajo palabra.</p>'''),
        ('linea-de-tiempo', 'De la captura al juez: la línea de tiempo', '''
<p>Así se ordenan las obligaciones que fija la ley, de la captura a la audiencia, y el documento que corresponde a cada una:</p>
<ol class="linea">
<li><span class="cuando">Al capturar</span><div><strong>Se descubre la flagrancia.</strong> Hay una de las cinco situaciones del art. 301. Cualquier persona puede capturar (art. 302).</div></li>
<li><span class="cuando">De inmediato</span><div><strong>Se informan los derechos.</strong> Los cuatro del art. 303. Queda en el <a href="acta-derechos-capturado-fpj6.html">FPJ-6</a>.</div></li>
<li><span class="cuando">De inmediato</span><div><strong>Identificación y registro.</strong> La policía judicial verifica identidad, capturas anteriores y antecedentes (parágrafo del art. 302). Los datos van idénticos en todos los documentos.</div></li>
<li><span class="cuando">Desde el hallazgo</span><div><strong>Cada elemento se rotula y entra a cadena de custodia.</strong> Un <a href="rotulo-elementos-fpj7.html">FPJ-7</a> por elemento y su <a href="cadena-de-custodia-fpj8.html">FPJ-8</a> (arts. 254 a 259).</div></li>
<li><span class="cuando">Al informar</span><div><strong>Se rinde el informe de la captura.</strong> El <a href="informe-captura-flagrancia-fpj5.html">FPJ-5</a> cuenta lo ocurrido y se pone a disposición de la Fiscalía.</div></li>
<li><span class="cuando">Máximo 36 horas</span><div><strong>Audiencia ante el juez de control de garantías.</strong> La Fiscalía presenta al aprehendido y se revisa la legalidad de la captura.</div></li></ol>
<p>¿Quieres los formatos para imprimirlos? Están en la página de <a href="descargas-formatos-fpj.html">descargas de los formatos FPJ en blanco</a>.</p>'''),
        ('no-flagrancia', 'Cuándo no hay flagrancia y qué pasa si la captura no se sostiene', '''
<p>Como lo que une las cinco situaciones del artículo 301 es la inmediatez, <strong>no hay flagrancia cuando ha pasado un tiempo que rompe la relación entre el hecho y la captura</strong>: sin persecución, sin que alguien señale a la persona de inmediato y sin objetos o huellas que indiquen que acaba de cometer el delito. En ese caso se necesita otra vía legal para capturar.</p>
<p>El artículo 302 también prevé qué ocurre si la captura no se sostiene: cuando de la información recogida aparezca que el supuesto delito <strong>no comporta detención preventiva</strong>, o que la captura fue <strong>ilegal</strong>, la Fiscalía ordena liberar al aprehendido y puede imponerle un compromiso de comparecencia bajo palabra.</p>
<div class="tip"><p><strong>Recomendación de redacción (no es un requisito legal):</strong> en la narración del informe deja clara la secuencia: cuándo y cómo se descubrió el hecho, cuándo y cómo se aprehendió a la persona y qué la relacionaba con el delito. Esa secuencia es la que muestra la inmediatez. Mira cómo hacerlo en <a href="como-redactar-la-narracion-de-los-hechos.html">cómo redactar la narración de los hechos</a>.</p></div>'''),
        ('documentos', 'Los documentos de una captura en flagrancia', '''
<div class="tabla"><table><thead><tr><th>Formato</th><th>Para qué sirve</th><th>Guía</th></tr></thead><tbody>
<tr><td>FPJ-5</td><td>Informe de Captura en Flagrancia: el relato completo del procedimiento, con datos del capturado, lugar, víctimas, testigos, elementos y narración.</td><td><a href="informe-captura-flagrancia-fpj5.html">Cómo diligenciarlo</a></td></tr>
<tr><td>FPJ-6</td><td>Acta de Derechos del Capturado: deja constancia de los derechos informados (art. 303) y de los datos personales.</td><td><a href="acta-derechos-capturado-fpj6.html">Cómo diligenciarlo</a></td></tr>
<tr><td>FPJ-7</td><td>Rótulo de elementos materiales probatorios y evidencia física: uno por cada elemento incautado.</td><td><a href="rotulo-elementos-fpj7.html">Cómo diligenciarlo</a></td></tr>
<tr><td>FPJ-8</td><td>Registro de Cadena de Custodia: quién halló, recolectó y embaló el elemento.</td><td><a href="cadena-de-custodia-fpj8.html">Cómo diligenciarlo</a></td></tr></tbody></table></div>
<p>Todos llevan el <strong>Número Único de Noticia Criminal (NUNC)</strong> y deben contar la misma historia: mismas personas, mismas fechas, mismo lugar. Si tienes que llenar todo a mano, la <a href="lista-de-chequeo-captura-flagrancia.html">lista de chequeo</a> ayuda a no olvidar nada.</p>'''),
    ],
    faq=[
        ('¿Qué es la flagrancia?', 'Es la situación en la que una persona es sorprendida cometiendo un delito o aprehendida inmediatamente después, o con objetos, huellas o en un vehículo que indican que acaba de cometerlo. El artículo 301 del Código de Procedimiento Penal enumera cinco situaciones.'),
        ('¿Qué pasa si la captura en flagrancia no se sostiene?', 'Según el artículo 302, si de la información aparece que el supuesto delito no comporta detención preventiva o que la captura fue ilegal, la Fiscalía libera al aprehendido y, cuando sea necesario, le impone un compromiso de comparecencia bajo palabra.'),
        ('¿Quién puede capturar a una persona en flagrancia?', 'Según el artículo 302 del Código de Procedimiento Penal, cualquier persona puede capturar a quien sea sorprendido en flagrancia. Si es una autoridad, debe conducirlo inmediatamente ante la Fiscalía; si es un particular, ante cualquier autoridad de policía.'),
        ('¿Cuánto tiempo hay para presentar al capturado ante el juez?', 'El artículo 302 dice que la Fiscalía lo presenta ante el juez de control de garantías inmediatamente o, a más tardar, dentro de las 36 horas siguientes. Hay una regla especial para zonas de difícil acceso por vía fluvial o geográfica.'),
        ('¿Cuáles son los derechos que se le leen al capturado?', 'El artículo 303 enumera cuatro: conocer el hecho que se le atribuye, indicar a quién se comunica su captura, guardar silencio (y saber que lo que diga podrá usarse en su contra) y designar un abogado de confianza o contar con defensor público.'),
        ('¿Qué documentos se diligencian en una captura en flagrancia?', 'Los formatos FPJ-5 (informe de captura), FPJ-6 (acta de derechos), FPJ-7 (rótulo) y FPJ-8 (cadena de custodia), todos con el mismo Número Único de Noticia Criminal.'),
    ],
    rel=['informe-captura-flagrancia-fpj5', 'rotulo-elementos-fpj7', 'descargas-formatos-fpj'],
    fuentes=['Ley 906 de 2004, artículos 301, 302 y 303 (texto consultado en noviembre de 2026): ' + LEY + '.', 'Corte Constitucional, <a href="https://www.corteconstitucional.gov.co/relatoria/2019/C-303-19.htm" rel="noopener">Sentencia C-303 de 2019</a>: la flagrancia se caracteriza por la inmediatez entre el hecho y la aprehensión.'],
)
PAGINAS = [INDEX, FLAGRANCIA]
