# Plan de campaña — llegar a los policías (borrador del 2026-10-30)

Estado de partida: **sin clientes reales todavía**, solo pruebas (el dueño empezó a ofrecer el producto hace poco). Hay 5 casos gratis, planes de $12.000 / $35.000 / $100.000 y un programa de referidos que funciona pero nadie conoce (Vikunja «Bot de Pagos» #62).
Esto es un borrador para que el dueño lo ajuste. Lo marcado con (?) son hipótesis a validar, no hechos.

## 1. La idea central

Los policías no compran «software»: buscan **sacar el informe sin errores y sin perder una hora**. Entonces la campaña no empieza vendiendo, empieza **ayudando a llenar los formatos**. Para eso están las 10 páginas del Centro de ayuda (`ayuda/`), que además sirven para que los encuentren en Google y los asistentes de IA. La venta va al final de cada página («prueba con 5 casos gratis»).

Regla de oro: **dar valor primero, vender después**. En un gremio unido, un mensaje comercial a pelo en un grupo cerrado quema la puerta; una guía útil que un compañero comparte, la abre.

## 2. Segmentos (hipótesis, (?) = validar con los usuarios de prueba)

| Segmento | Por qué le sirve | Plan probable |
|---|---|---|
| Patrullero o uniformado que captura | Llena los cuatro formatos tras un procedimiento, muchas veces cansado | Mensual $35.000 (con IA de redacción) |
| Policía judicial / investigador (?) | Más volumen de formatos y cadena de custodia | Mensual |
| Quien solo captura de vez en cuando | Un informe suelto cada cierto tiempo | Semanal $12.000 |
| Estación, grupo o jefe de turno (?) | Varios uniformados, quiere uniformidad | Negocio/Estación $100.000 |
| Estudiantes de formación (?) | Aprenden los formatos | Contenido gratis; no es el cliente de pago |

**Primera tarea de validación:** preguntarle a los usuarios de prueba (por WhatsApp, con 3 preguntas) cómo llegaron, qué les molesta de llenar los formatos y a quién se lo mostrarían. Con 5 respuestas el plan se ajusta mejor que con cualquier suposición mía.

## 3. Canales

**Lo que sí podemos hacer sin riesgo**
1. **Google y asistentes de IA** — Centro de ayuda + `llms.txt` + sitemap. Es el canal que trabaja solo mientras duermes. Medir a 30 días.
2. **YouTube** — los 4 videos tutoriales (ya hay guiones en `GUIONES_VIDEOS.md`, tarea #163). Cada video apunta a una página de ayuda.
3. **Videos cortos (TikTok, Reels, Shorts)** — «el error del FPJ-8 que más se repite», «cómo se escribe bien la hora», «tres cosas para revisar antes de firmar». Una idea por video, 30 a 45 segundos, con datos inventados.
4. **Boca a boca y referidos** — el programa de referidos ya existe. Falta que se vea: ponerlo en la landing y en el mensaje de entrega (Vikunja #62).
5. **Demostración presencial** — mostrarlo en una estación o a un grupo de compañeros con confianza (? depende del acceso del dueño).

**Facebook, Instagram y WhatsApp (grupos y páginas de policías)**
- Los grupos cerrados **no se pueden buscar desde afuera** y no inventamos nombres. Se identifican desde adentro: por el dueño, sus conocidos y los usuarios de prueba. Cuando haya una lista real, la anotamos aquí.
- Cómo entrar: como persona real, leer las reglas, pedirle permiso al administrador y **aportar primero** (una guía, una lista de chequeo). Nunca mensajes masivos ni «links en todos los grupos».
- Meta (Facebook/Instagram) permite pauta segmentada por intereses y ubicación; no hay un segmento «policía» garantizado. Probar con un presupuesto mínimo solo después de tener contenido que convierta (?).

## 4. Mensajes

- **Dolor:** «Cuatro formatos, los mismos datos escritos cuatro veces.»
- **Promesa:** «Llena el caso una vez y se generan todos, con el mismo nombre, la misma hora y la misma descripción.»
- **Prueba:** «5 casos gratis, sin tarjeta. Funciona sin internet.»
- **Confianza:** «Herramienta independiente: no es oficial ni está avalada por la Policía.» (Siempre. Es lo que dice la landing y evita problemas.)

## 5. Calendario de 4 semanas (12 publicaciones, listas para ajustar)

Cada una enlaza a su página de ayuda y lleva `?ref=` del canal para medir.

| # | Semana | Tema | Idea del texto | Página |
|---|---|---|---|---|
| 1 | 1 | Presentación del Centro de ayuda | «Armamos guías para llenar bien los formatos FPJ. Gratis.» | `ayuda/` |
| 2 | 1 | El error del nombre | «Si el nombre está escrito distinto en dos formatos, se nota.» | errores comunes |
| 3 | 1 | Hora de la captura | «La hora del FPJ-5 tiene que coincidir con la del acta de derechos.» | FPJ-5 |
| 4 | 2 | Los 4 derechos del art. 303 | Infografía simple con los cuatro derechos | FPJ-6 |
| 5 | 2 | Marcas H, R y E | «¿Quién halló, quién recolectó, quién embaló?» | FPJ-8 |
| 6 | 2 | Lista imprimible | «Imprímela y llévala» | lista de chequeo |
| 7 | 3 | Narración en 7 pasos | Carrusel con el orden cronológico | narración |
| 8 | 3 | Descripción de un elemento | Antes y después de una descripción | FPJ-7 |
| 9 | 3 | 36 horas | «Qué dice el art. 302 sobre el plazo» | flagrancia |
| 10 | 4 | Desde el celular | Demo corta de la app generando los documentos | desde el celular |
| 11 | 4 | Referidos | «Si le sirvió a un compañero, ganas días» (cuando el programa sea visible) | landing |
| 12 | 4 | Preguntas | Respuestas a las dudas que lleguen | FAQ |

## 6. Medición

- Cloudflare Web Analytics ya está en todas las páginas (también en `ayuda/`). Revisar cuántas visitas llegan a cada guía.
- Enlaces con `?ref=youtube`, `?ref=tiktok`, `?ref=fb`, etc. (verificar que Cloudflare los separe; si no, usar páginas con alias).
- Una sola meta: **personas que prueban los 5 casos** y luego pagan. Todo lo demás es ruido.
- Revisión mensual con `growth-pulse` o a mano.

## 7. Cuidados

- Nunca publicar datos reales de capturados: solo datos inventados, como en las muestras.
- No dar a entender que la Policía o la Fiscalía avalan el producto.
- Una lista de contactos con teléfonos exige autorización de las personas (Ley 1581 de 2012, habeas data).
- Contenido jurídico: citar el artículo y recordar que manda el instructivo oficial.

## 8. Decisiones del dueño

1. ¿Hay presupuesto para pauta pagada? (si no, el plan sigue funcionando.)
2. ¿Puede aparecer él o un compañero en los videos o prefiere solo pantalla y voz?
3. ¿Qué segmentos ve más cerca?
4. Lista real de grupos y páginas donde ya hay conocidos.
