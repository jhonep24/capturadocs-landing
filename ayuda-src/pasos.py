# Paso a paso interactivo: (título, a mano, con CapturaDocs Express). Solo lo que la landing ya sostiene
# (un formulario, mismos datos en todos los documentos, validación antes de generar). Sin cifras de tiempo.
PASOS = {
 'informe-captura-flagrancia-fpj5': ('Llenar el FPJ-5', [
  ('Encabezado y NUNC', 'Escribes el NUNC dígito por dígito y lo repites en cada formato.', 'Lo escribes una vez en el caso y sale igual en el FPJ-5, 6, 7 y 8.'),
  ('Destino, conducta y lugar', 'Redactas la URI de destino, el delito con su artículo y la dirección de los hechos.', 'Los llenas en el formulario por pasos y quedan guardados para los demás documentos.'),
  ('Capturado, víctimas y testigos', 'Repites nombres, documento y datos personales en cada sección.', 'Registras a cada persona una sola vez; sus datos se reutilizan.'),
  ('Narración, fecha y hora', 'Escribes el relato y cuidas que la hora coincida con el acta de derechos.', 'La fecha y la hora se escriben una vez y coinciden en todos los formatos.'),
  ('Revisar y firmar', 'Revisas casilla por casilla para no dejar nada vacío.', 'La aplicación te avisa lo que falta antes de generar. Imprimes y firmas.')]),
 'acta-derechos-capturado-fpj6': ('Llenar el FPJ-6', [
  ('Encabezado y NUNC', 'Copias el NUNC del informe, con el riesgo de cambiar un dígito.', 'Sale del mismo caso del FPJ-5, sin copiarlo.'),
  ('Datos del capturado', 'Vuelves a escribir nombre, documento, edad y fecha de nacimiento.', 'Se toman del caso: no se retipean.'),
  ('Los derechos del art. 303', 'Transcribes o marcas el texto de los derechos.', 'El texto de los derechos ya viene en el formato.'),
  ('Constancia de buen trato', 'Repites nombre, documento y delito para la constancia.', 'La constancia repite los datos exactamente como en el informe.'),
  ('Revisar y firmar', 'Verificas que fecha y hora coincidan con el FPJ-5.', 'Coinciden porque se escribieron una sola vez. Imprimes y firmas.')]),
 'rotulo-elementos-fpj7': ('Llenar el FPJ-7', [
  ('Un rótulo por elemento', 'Preparas un rótulo por cada elemento incautado.', 'Agregas cada elemento en el caso y se genera un rótulo por cada uno.'),
  ('NUNC, fecha y hora de recolección', 'Los escribes de nuevo en cada rótulo.', 'Se toman del caso.'),
  ('Sitio y persona a quien se halló', 'Repites dirección y nombre de la persona.', 'Los datos del capturado y del lugar se reutilizan.'),
  ('Descripción del elemento', 'La redactas aquí y otra vez en el informe y la cadena de custodia.', 'La escribes una vez y sale idéntica en los tres documentos.'),
  ('Imprimir y pegar', 'Imprimes y recortas cada rótulo.', 'La guía de uso explica cómo imprimirlo en tamaño reducido para el embalaje.')]),
 'cadena-de-custodia-fpj8': ('Llenar el FPJ-8', [
  ('NUNC e identificación', 'Escribes el NUNC y el número de ID del elemento.', 'Salen del caso, iguales a los del rótulo.'),
  ('Marcas H, R y E', 'Marcas quién halló, recolectó y embaló, con cuidado de que cuadre.', 'Registras quién intervino en cada etapa y pasa al formato.'),
  ('Nombres, cédulas y entidad', 'Los repites por cada persona que interviene.', 'Los escribes una vez por servidor y se reutilizan en todos los documentos.'),
  ('Descripción del elemento', 'La copias a mano del rótulo.', 'Es idéntica a la del rótulo y a la del informe, sin copiarla.'),
  ('Fechas y firmas', 'Revisas que cada firma tenga su fecha.', 'La aplicación te avisa lo que falta antes de generar. Imprimes y firmas.')]),
 'captura-en-flagrancia-colombia': ('Documentar la captura', [
  ('Informar los derechos (FPJ-6)', 'Llenas el acta con los datos del capturado.', 'Sale del caso, con los datos ya cargados.'),
  ('Informe de captura (FPJ-5)', 'Redactas el informe repitiendo nombres, NUNC y hora.', 'Sale del mismo caso, con los mismos datos.'),
  ('Rotular los elementos (FPJ-7)', 'Un rótulo por elemento, con la descripción otra vez.', 'Un rótulo por elemento, con la descripción ya escrita.'),
  ('Cadena de custodia (FPJ-8)', 'Registras cada intervención y copias de nuevo los datos.', 'Se genera con los mismos datos del rótulo y del informe.'),
  ('Poner a disposición (36 horas)', 'Revisas que todo coincida antes de presentarlo.', 'La aplicación avisa lo que falta antes de generar los cuatro documentos.')]),
}
# PDF de ejemplo (datos inventados) por página: (archivo, formato, nombre, hojas)
PDFS = {
 'informe-captura-flagrancia-fpj5': ('ejemplo-fpj5-diligenciado.pdf', 'FPJ-5', 'Informe de Captura', 3),
 'acta-derechos-capturado-fpj6': ('ejemplo-fpj6-diligenciado.pdf', 'FPJ-6', 'Acta de Derechos', 2),
 'rotulo-elementos-fpj7': ('ejemplo-fpj7-diligenciado.pdf', 'FPJ-7', 'Rótulo', 1),
 'cadena-de-custodia-fpj8': ('ejemplo-fpj8-diligenciado.pdf', 'FPJ-8', 'Cadena de Custodia', 2),
 'informe-primer-respondiente-fpj4': ('formato-fpj4-en-blanco.pdf', 'FPJ-4', 'Actuación del Primer Responsable', 4),
}
