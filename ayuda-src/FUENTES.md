# Centro de ayuda: de dónde sale cada afirmación (auditoría 2026-11-22)

Regla: una afirmación jurídica o sobre un formato se publica solo si se puede señalar su fuente. Lo que es consejo
de redacción o buena práctica se rotula como tal («sugerencia», «buena práctica»).

## Fuentes primarias consultadas
- **Ley 906 de 2004** (Secretaría del Senado, texto con modificaciones): arts. 128, 254 a 259, 301 (mod. Ley 1453/2011),
  302 (+ Ley 1142/2007, Ley 2111/2021) y 303. Contrastados el 2026-11-22 frase por frase.
- **Formatos oficiales** (plantillas `informes-ponal/public/plantillas/fpj4..fpj8.docx`, pie de página y texto impreso):
  FPJ-4 v04 (aprob. 2022-07-26, publ. 2022-08-19), FPJ-5 v04 (2019-08-28 / 2019-09-03), FPJ-6 v03 (2022-07-26 / 2022-08-19),
  FPJ-7 v04 y FPJ-8 v04 (2018-04-18 / 2018-12-27). Las tablas de casillas de cada guía salen de ahí.
- **Corte Constitucional, Sentencia C-303 de 2019**: la flagrancia exige inmediatez (cita en la página de flagrancia).
- **Precios, planes y funciones de la app**: `index.html` (tarjetas de planes y condiciones).

## No se pudo verificar (los PDF de la Fiscalía devuelven 404)
Manual del Sistema de Cadena de Custodia, Manual Único de Policía Judicial e instructivos de diligenciamiento FPJ-4 a FPJ-8.
Por eso las guías NO afirman cómo se asigna el «No. ID», ni cómo se escribe la hora más allá de lo que trae el formato,
ni reglas de actuación del primer responsable más allá de las preguntas del formato.
Si algún día se consiguen los instructivos, contrastar: FPJ-4 (secciones 2 y 3), «No. ID» de FPJ-7/FPJ-8 y hora del FPJ-7.

## Correcciones hechas en esta auditoría
- Art. 303 (FAQ de flagrancia y FPJ-6): el silencio y «lo que diga podrá usarse en su contra» se citaban mal.
- «Informe detallado» del art. 302 lo rinde el particular a la autoridad; ya no se dice que sea el FPJ-5.
- FPJ-8: faltaban las casillas 6 (registro de continuidad), 7 (PIPH) y 8 (observaciones); la fecha no está en la casilla 4.
- FPJ-7: la casilla 5 pide solo nombres y apellidos de la persona (no documento); sin «24 horas» ni instructivo inventado.
- Lista de chequeo: la cadena de custodia no pide «firma con fecha» en cada fila. (Aquí decía también que el acta FPJ-6 no tiene «lugar»:
  es un error de esta nota; la plantilla `fpj6.docx` v03 y el PDF en blanco sí traen «Lugar:» junto a fecha y hora — verificado 2026-11-27.)
- Retiradas afirmaciones sin sustento: «toma la mitad del tiempo», «errores más comunes/frecuentes», «hacen devolver un informe»,
  «menos devoluciones», «la central de radio asigna el CAD» y los consejos del primer responsable que no salían del formato.
- Tabla de planes (página «desde el celular»): el soporte por WhatsApp es del plan mensual, no del Negocio/Estación.

## Carrusel «casilla por casilla» (2026-11-26/27)
- Los pasos (`carrusel_fpjN.py`) salen del **texto impreso** de cada formato (PDF en blanco de `ayuda/pdf/`, leído con PyMuPDF)
  y de lo que ya estaba contrastado en las guías. Las cajas se dibujaron sobre la hoja y se revisaron una por una.
- Ejemplos: datos inventados, rotulados «Ejemplo:». Consejos propios: rotulados «Sugerencia».
- Sin resolver (se dice en el paso y se remite al instructivo o al fiscal): en la constancia de buen trato del FPJ-6, cuál de los
  espacios «indiciado(a)» / «imputado(a)» se completa; cómo se asigna el «No. ID» del FPJ-7 y del FPJ-8.
- El orden de la fecha del FPJ-5 (encabezado, tres casillas sin rótulo) no se afirma; en FPJ-4 y FPJ-8 sí viene impreso (AAAA MM DD).
