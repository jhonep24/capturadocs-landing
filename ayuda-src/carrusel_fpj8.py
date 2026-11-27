# Carrusel casilla por casilla del FPJ-8 (Registro de Cadena de Custodia, versión 04, 2 hojas horizontales).
# Misma estructura que carrusel_fpj6.py. Cajas en puntos del PDF oficial (hoja de 792 x 612).
# Las instrucciones salen del texto impreso del formato (convenciones y notas) y de la guía de la página (FUENTES.md).
PAGINA = (792, 612)

PASOS = [
 dict(h=1, caja=(101, 64, 507, 110), t='Qué es este formato',
      texto='El <strong>Registro de Cadena de Custodia</strong> (FPJ-8) es el historial del elemento: quién lo halló, lo recolectó y lo embaló, y quién lo ha recibido después. Es la versión 04 y tiene <strong>dos hojas horizontales</strong>. Los formatos FPJ-7 y FPJ-8 son exclusivos para la función de Policía Judicial.'),
 dict(h=1, caja=(46, 64, 707, 162), t='Casillas 1, 2 y 3: NUNC, No. ID e historia clínica',
      texto='<strong>1.</strong> El Número Único de Noticia Criminal, un dígito por casilla (DPTO, MUNICIPIO, ENTIDAD, UNIDAD, AÑO y CONSECUTIVO). <strong>2.</strong> El No. ID, una cifra por casilla. <strong>3.</strong> El número de historia clínica lleva un asterisco: según las convenciones, lo diligencia la entidad prestadora de salud que recolecte el elemento; si no es el caso, queda en blanco.',
      sug='El NUNC debe ser idéntico al de los demás formatos. Para el No. ID, consulta el instructivo de tu institución.'),
 dict(h=1, caja=(46, 165, 750, 326), t='Casilla 4: documentación de los elementos (H, R y E)',
      texto='Una fila por cada persona que interviene: marca con una X <strong>H</strong> si <strong>halló</strong>, <strong>R</strong> si <strong>recolectó</strong> o <strong>E</strong> si <strong>embaló</strong> el elemento (se pueden marcar una o varias opciones para un mismo nombre), y escribe sus <strong>nombres y apellidos</strong>, <strong>cédula de ciudadanía</strong>, <strong>entidad</strong> y <strong>firma</strong>.',
      ej='H, R y E marcadas · Carlos Andrés Ramírez Díaz · C.C. 1.020.345.678 · PONAL',
      sug='Si la misma persona hizo las tres tareas, marca las tres en su fila; si fueron distintas, cada una lleva la suya.'),
 dict(h=1, caja=(46, 331, 750, 467), t='Casilla 5: descripción del elemento',
      texto='Describe el elemento material probatorio o la evidencia física en las líneas del recuadro.',
      ej='Teléfono celular marca X, color negro, pantalla sin fisuras, IMEI 000000000000000',
      sug='Debe ser igual a la del rótulo (FPJ-7), a la del informe (FPJ-5, sección 7) y a la del embalaje.'),
 dict(h=1, caja=(46, 480, 750, 523), t='Convenciones impresas',
      texto='Al pie de la hoja el formato recuerda tres cosas: el asterisco (*) indica que esa casilla la diligencia la entidad prestadora de salud que recolecte el elemento; H, R y E se marcan con una X según quien halló, recolectó o embaló; y los formatos de rótulo y de cadena de custodia (FPJ-7 y FPJ-8) son exclusivos para la función de Policía Judicial.'),
 dict(h=2, caja=(49, 20, 459, 106), t='Casilla 6 (1): registro de continuidad, quién y cuándo',
      texto='Cada vez que el elemento pasa a otra persona se llena una fila. Primero la <strong>fecha</strong> (AAAA, MM, DD), la <strong>hora</strong>, los <strong>nombres y apellidos de quien recibe</strong> el EMP y EF, su <strong>cédula</strong> y su <strong>entidad</strong>.',
      ej='2026 03 15 · 1730 · Luis Gómez Pérez · C.C. 80.000.000 · PONAL',
      sug='La fecha del primer traspaso no debe ser anterior a la de recolección del FPJ-7.'),
 dict(h=2, caja=(459, 20, 740, 106), t='Casilla 6 (2): calidad, propósito, estado y firma',
      texto='<strong>Calidad en la que actúa</strong>: C (custodio) o P (perito). <strong>Propósito del traslado</strong>: almacenamiento, análisis, presentación en audiencia, consulta o disposición final. <strong>Estado en que se recibe el embalaje o contenedor</strong> del EMP y EF, y <strong>firma</strong> de quien recibe.',
      ej='C · Almacenamiento · Embalaje sellado, sin daños'),
 dict(h=2, caja=(49, 310, 202, 455), t='Casilla 7: prueba de identificación preliminar (PIPH)',
      texto='Solo la diligencia el <strong>técnico en prueba de identificación preliminar homologada</strong> (PIPH): si practicó la prueba (SI o NO), la <strong>cantidad de muestras tomadas</strong> y el <strong>número de rótulo(s)</strong>. Si no hubo prueba, queda en blanco.'),
 dict(h=2, caja=(216, 310, 740, 455), t='Casilla 8: observaciones',
      texto='Espacio para observaciones. El formato indica que, cuando se registren, se escriben el <strong>nombre de quien las realiza</strong> y la <strong>fecha</strong>.'),
 dict(h=2, caja=(49, 463, 740, 502), t='Notas del formato',
      texto='Impresas en la hoja: <strong>1)</strong> nunca interrumpa el registro de cadena de custodia; <strong>2)</strong> el registro siempre debe acompañar a los elementos; <strong>3)</strong> si la hoja no alcanza, se diligencia el registro de continuidad con el formato adicional de registro de cadena de custodia (FPJ-8); <strong>4)</strong> cuando se registren observaciones, se escriben el nombre de quien las realiza y la fecha.'),
 dict(h=2, caja=None, t='Revisión antes de firmar',
      texto='Comprueba: marcas <strong>H, R y E</strong> solo donde la persona hizo esa tarea, y una fila por cada persona que intervino; cada traspaso registrado en el <strong>registro de continuidad</strong>; <strong>descripción</strong> igual a la del rótulo y la del informe; <strong>nombre y cédula</strong> escritos igual que en el resto de documentos; y la historia clínica en blanco si no corresponde.'),
]
