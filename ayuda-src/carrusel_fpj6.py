# Carrusel casilla por casilla del FPJ-6 (Acta de Derechos del Capturado, versión 03).
# Cada paso: h = hoja (1 o 2); caja = (x0, y0, x1, y1) en puntos del PDF oficial (hoja de 612 x 792) o None;
# t = título corto; texto = qué es y qué se escribe (sale del formato oficial y del art. 303 de la Ley 906);
# ej = ejemplo con datos INVENTADOS; sug = sugerencia/buena práctica (rotulada como tal en la página).
# Tono: de colega a colega, directo, sin explicar lo obvio. Los pasos agrupan casillas afines (15 en total).
PAGINA = (612, 792)
ANCHO_TABLA = (43, 570)


def fila(y0, y1):
    return (ANCHO_TABLA[0], y0, ANCHO_TABLA[1], y1)


PASOS = [
 dict(h=1, caja=(49, 129, 564, 165), t='Qué es este formato',
      texto='El <strong>Acta de Derechos del Capturado</strong> (FPJ-6) deja constancia de que se le informaron al capturado sus derechos y recoge sus datos personales. Tiene <strong>dos hojas</strong> y se llena <strong>una por cada persona capturada</strong>.'),
 dict(h=1, caja=(43, 65, 570, 115), t='Encabezado: NUNC y radicado interno',
      texto='A la derecha va el <strong>NUNC</strong> (Número Único de Noticia Criminal), una cifra en cada casilla y por grupos: Dpto., Municipio, Entidad, Unidad Receptora, Año y Consecutivo. A la izquierda, el <strong>radicado interno</strong> de tu entidad, si lo maneja.',
      sug='Escribe el NUNC igual al del FPJ-5: un dígito distinto hace que los formatos no coincidan.'),
 dict(h=1, caja=(43, 181, 534, 196), t='Fecha, hora y lugar',
      texto='La <strong>fecha</strong> va por día (D), mes (M) y año (A); la <strong>hora</strong>, en cuatro casillas (horas y minutos); el <strong>lugar</strong>, en la línea siguiente. Se anota la hora en que se le leyeron los derechos, porque el artículo 303 dice que se le hacen saber de manera <strong>inmediata</strong>.',
      ej='15/03/2026, 14:35, Bogotá D.C., CAI Santa Fe',
      sug='Que fecha, hora y ciudad coincidan con las del informe de captura (FPJ-5).'),
 dict(h=1, caja=(43, 208, 571, 335), t='Los cuatro derechos (ya impresos)',
      texto='Este bloque viene impreso y no se llena. Recoge lo que dice el artículo 303: <strong>1.</strong> el hecho atribuido y quién ordenó la captura; <strong>2.</strong> poder indicar a quién se avisa de la captura; <strong>3.</strong> guardar silencio, que lo que diga puede usarse en su contra y que no está obligado a declarar contra su cónyuge, compañero(a) permanente o parientes cercanos; <strong>4.</strong> designar abogado de confianza y comunicarse con él cuanto antes o, si no puede, contar con la defensa pública.',
      sug='Léelos completos y en voz clara antes de pasar a los datos.'),
 dict(h=1, caja=fila(387, 447), t='Datos personales (1): identidad',
      texto='Empieza el punto 1, «Mis datos personales son». Se escriben tal como los da la persona y se comparan con su documento: <strong>nombres y apellidos completos</strong> e <strong>identificación</strong> (tipo, número y lugar de expedición). La casilla de <strong>nombre identitario</strong> es solo para personas trans; si no aplica, queda en blanco.',
      ej='Juan Carlos Pérez Gómez · C.C. 10.000.000 de Bogotá',
      sug='Copia el nombre y el número tal cual están en el documento.'),
 dict(h=1, caja=fila(448, 542), t='Datos personales (2): nacimiento y familia',
      texto='<strong>Fecha</strong> y <strong>lugar de nacimiento</strong>, <strong>nombre de los padres</strong>, <strong>estado civil</strong> y <strong>ocupación u oficio</strong>.',
      ej='3 de julio de 1990 · Medellín, Antioquia · Pedro Pérez y Marta Gómez · Soltero · Mecánico',
      sug='La fecha de nacimiento debe quedar escrita igual en el FPJ-5, aquí y en la constancia de buen trato.'),
 dict(h=1, caja=fila(543, 596), t='Datos personales (3): contacto',
      texto='<strong>Dirección y teléfono</strong>, <strong>correo electrónico</strong> y <strong>redes sociales</strong>.',
      ej='Calle 10 # 5-20, barrio Centro · 300 000 0000 · nombre@ejemplo.com',
      sug='Si la persona no tiene correo o redes, déjalo sin llenar o anota que no tiene; no lo completes por tu cuenta.'),
 dict(h=1, caja=fila(597, 695), t='Autoidentificación y «he entendido»',
      texto='Las preguntas sobre <strong>persona LGBTI</strong> (SI/NO y ¿CUÁL?), <strong>pertenencia étnica</strong> (indígena, negro/a, raizal, afrocolombiano, palenquero/a o RROM) y <strong>comunidad</strong> las responde la persona; se marca o escribe lo que ella diga. Al final, el punto 2 («Que he entendido los derechos leídos») ya viene impreso. Sigue la segunda hoja.'),
 dict(h=2, caja=(43, 63, 570, 158), t='A quién se avisa de la captura',
      texto='Punto 3, el derecho número 2 del artículo 303. Se escriben <strong>nombres, apellidos e identificación</strong> de la persona que el capturado indique, su <strong>teléfono</strong> y la <strong>hora</strong> en que se le comunicó la captura.',
      ej='María Gómez, C.C. 20.000.000 · 310 000 0000 · 14:50'),
 dict(h=2, caja=(43, 160, 570, 215), t='Observaciones',
      texto='Dos líneas para lo que haga falta dejar constancia. Si no hay nada que anotar, quedan en blanco.',
      sug='Si el capturado no quiere firmar, déjalo anotado aquí.'),
 dict(h=2, caja=(43, 247, 535, 340), t='Firmas del acta',
      texto='A la izquierda, <strong>firma y/o huella del capturado</strong> (el cuadro es para la huella). A la derecha, dos líneas para <strong>nombre, cédula y firma</strong> de los servidores.'),
 dict(h=2, caja=(43, 364, 570, 497), t='Constancia de buen trato',
      texto='Es un texto con espacios para completar. En ella el capturado manifiesta que recibió buen trato físico, psicológico y moral del personal que hizo la captura, y que se le comunicaron y respetaron sus derechos. Repite datos que ya escribiste.'),
 dict(h=2, caja=(43, 399, 570, 442), t='Constancia: lugar, fecha y datos del capturado',
      texto='Primera línea: <strong>ciudad</strong>, <strong>días</strong>, <strong>mes</strong>, <strong>año</strong> y <strong>hora</strong>. Después, «el señor(a)»: <strong>nombre completo</strong>, <strong>documento</strong>, <strong>fecha de nacimiento</strong>, <strong>edad</strong> y <strong>estado civil</strong>, iguales a los del punto 1.',
      ej='En Bogotá a los 15 días, del mes de marzo del año 2026, siendo las 14:35 horas; el señor Juan Carlos Pérez Gómez, identificado con C.C. 10.000.000, nacido el 3 de julio de 1990, de 35 años, soltero',
      sug='Ciudad, fecha y hora deben coincidir con las del FPJ-5.'),
 dict(h=2, caja=(43, 442, 570, 496), t='Constancia: indiciado o imputado, y delito',
      texto='Hay un espacio junto a «<strong>indiciado(a)</strong>» y otro junto a «<strong>imputado(a)</strong>», y una línea después de «<strong>del delito de</strong>» para el nombre del delito. El texto que sigue («suscribe la presente acta con el fin de manifestar el buen trato…») ya viene impreso.',
      sug='Escribe el delito igual que en el FPJ-5. Si dudas cuál de los dos espacios corresponde, consulta el instructivo oficial vigente o a tu fiscal.'),
 dict(h=2, caja=(43, 517, 566, 671), t='Firmas finales',
      texto='Bajo «En constancia firman:» van la <strong>firma y la huella del capturado</strong>, y en la línea larga el <strong>nombre, código, cargo y firma del fiscal</strong>. El aviso del final ya viene impreso: el servidor de policía judicial debe garantizar <strong>en todo tiempo la reserva de la información</strong>.'),
 dict(h=2, caja=None, t='Revisión antes de firmar',
      texto='Antes de firmar comprueba: <strong>nombre</strong> igual al del documento; <strong>fecha de nacimiento</strong> igual en las tres partes; <strong>ciudad, fecha y hora</strong> iguales a las del FPJ-5; firmas del capturado, de los servidores y del fiscal.',
      sug='Con CapturaDocs Express estos datos se escriben una sola vez y salen iguales en todos los formatos.'),
]
