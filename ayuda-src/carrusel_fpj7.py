# Carrusel casilla por casilla del FPJ-7 (Rótulo de EMP y EF, versión 04, una hoja horizontal).
# Misma estructura que carrusel_fpj6.py. Cajas en puntos del PDF oficial (hoja de 842 x 596).
# Las instrucciones salen del texto impreso del formato y de la guía de la página (contrastada con FUENTES.md).
PAGINA = (842, 596)

PASOS = [
 dict(h=1, caja=(140, 64, 466, 82), t='Qué es este formato',
      texto='El <strong>Rótulo de Elementos Materiales Probatorios y Evidencia Física</strong> (FPJ-7) identifica cada elemento que se recolecta. Es la versión 04, en <strong>una sola hoja horizontal</strong>. Se llena <strong>un rótulo por cada elemento</strong>: si se recogieron un celular y una billetera, son dos rótulos. Los formatos FPJ-7 y FPJ-8 son exclusivos para la función de Policía Judicial.'),
 dict(h=1, caja=(67, 112, 462, 154), t='Casilla 1: NUNC',
      texto='El <strong>Número Único de Noticia Criminal</strong>, un dígito por casilla y por grupos: DPTO, MUNICIPIO, ENTIDAD, UNIDAD, AÑO y CONSECUTIVO.',
      sug='Debe ser idéntico al de los demás formatos del caso.'),
 dict(h=1, caja=(516, 64, 706, 96), t='Casilla 2: No. ID',
      texto='Casilla de identificación del rótulo, con una cifra por casilla.',
      sug='Consulta en el instructivo de tu institución cómo se asigna este número.'),
 dict(h=1, caja=(498, 112, 742, 141), t='Casilla 3: fecha y hora de recolección',
      texto='La fecha va en ocho casillas (año, mes y día) y la hora en cuatro: dos para la hora y dos para los minutos.',
      ej='2026 03 15 · 1430 (las 14:30)'),
 dict(h=1, caja=(67, 163, 129, 280), t='Casilla 4: hallazgo',
      texto='El <strong>número del EMP y EF</strong> y la <strong>cantidad</strong>.',
      ej='Número 01 · Cantidad 1'),
 dict(h=1, caja=(149, 163, 461, 280), t='Casilla 5: sitio o lugar de hallazgo',
      texto='La <strong>dirección</strong> donde se encontró el elemento y su <strong>ubicación</strong> dentro del lugar.',
      ej='Dirección: Carrera 7 # 45-12, Bogotá · Ubicación: bolsillo derecho del pantalón'),
 dict(h=1, caja=(498, 170, 761, 280), t='Casilla 5 (derecha): persona a quien se le encontró',
      texto='<strong>Nombres y apellidos de la persona a quien se le encontró</strong> el EMP y EF.',
      ej='Carlos Andrés Ramírez Díaz',
      sug='Escríbelo igual que en el FPJ-5 y el FPJ-6.'),
 dict(h=1, caja=(67, 286, 761, 427), t='Casilla 6: descripción del elemento',
      texto='Describe el elemento material probatorio o la evidencia física en las líneas del recuadro.',
      ej='Teléfono celular marca X, color negro, pantalla sin fisuras, IMEI 000000000000000',
      sug='Describe de modo que alguien que nunca vio el elemento pueda reconocerlo: qué es, marca, modelo, color, seriales y estado. Escríbela una vez y cópiala igual al FPJ-5 (sección 7), al FPJ-8 (casilla 5) y al embalaje.'),
 dict(h=1, caja=(67, 433, 761, 473), t='Casilla 7: rótulo diligenciado por',
      texto='<strong>Nombres y apellidos</strong>, <strong>cédula de ciudadanía</strong>, <strong>entidad</strong>, <strong>cargo</strong> y <strong>firma</strong> de quien diligencia el rótulo.'),
 dict(h=1, caja=None, t='Revisión antes de firmar',
      texto='Comprueba: <strong>NUNC</strong> igual al de los demás formatos; <strong>fecha y hora</strong> de recolección coherentes con el FPJ-5 y el FPJ-8; <strong>descripción</strong> idéntica en los tres; <strong>nombre</strong> de la persona escrito igual que en los otros documentos; y un rótulo por cada elemento.',
      sug='Con CapturaDocs Express la descripción se escribe una vez y sale igual en el FPJ-5, el FPJ-7 y el FPJ-8.'),
]
