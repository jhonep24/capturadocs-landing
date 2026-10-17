// Capturas de la guía paso a paso. Todo con datos inventados y red simulada.
// Salida: PNG en GUIA_OUT, numerados en el orden en que aparecen en el PDF.
import { test } from '@playwright/test';
import { prepararRed, primerIngreso, resaltar, acercar, quitarResaltes, foto } from './util-guia.js';

const campos = (page) => page.locator('input:visible, textarea:visible, select:visible');
const etiqueta = (page, re) => page.locator('label', { hasText: re }).first();
const arriba = (page) => page.evaluate(() => window.scrollTo(0, 0));
const paso = async (page, nombre) => {
  await page.getByRole('button', { name: new RegExp(`${nombre}\\s*$`) }).first().click();
  await page.waitForTimeout(600);
};

test('capturas de la guia', async ({ page }) => {
  await prepararRed(page);

  // 01-03: términos, correo y configuración inicial (la propia función captura)
  await primerIngreso(page, { capturar: true });

  // 04: pantalla principal (Inicio)
  const tarjeta = page.getByRole('button', { name: /^Captura en flagrancia/ });
  await tarjeta.waitFor();
  await arriba(page);
  await resaltar(page, tarjeta, 1);
  await resaltar(page, page.getByRole('button', { name: /Encabezado\s*$/ }).first(), 2);
  await resaltar(page, page.getByText(/Modo prueba/).first(), 3);
  await resaltar(page, page.getByRole('button', { name: /Guardar$/ }).first(), 4);
  await foto(page, '04-pantalla-principal');
  await quitarResaltes(page);
  await tarjeta.click();
  await page.waitForTimeout(400);

  // 05: Encabezado
  await paso(page, 'Encabezado');
  await campos(page).nth(5).fill('HURTO (ART. 239 C.P.)');
  await campos(page).nth(5).press('Tab');
  await campos(page).nth(8).fill('CALLE 1 # 2-34');
  await campos(page).nth(9).fill('BARRIO EJEMPLO');
  await arriba(page);
  await resaltar(page, etiqueta(page, /^NUNC/i), 1);
  await resaltar(page, etiqueta(page, /^PRESUNTO DELITO 1/i), 2);
  await foto(page, '05-encabezado');
  await quitarResaltes(page);

  // 06: Capturados
  await paso(page, 'Capturados');
  await campos(page).nth(0).fill('JUAN');
  await campos(page).nth(1).fill('CARLOS');
  await campos(page).nth(2).fill('PEREZ');
  await campos(page).nth(3).fill('GOMEZ');
  await campos(page).nth(5).fill('1000000001');
  await campos(page).nth(6).fill('BOGOTA');
  await campos(page).nth(7).fill('1990-05-20');
  await campos(page).nth(12).fill('COMERCIANTE');
  await arriba(page);
  await resaltar(page, etiqueta(page, /^PRIMER NOMBRE/i), 1);
  await resaltar(page, etiqueta(page, /^NO\. DOCUMENTO/i), 2);
  await foto(page, '06-capturados');
  await quitarResaltes(page);

  // 07: Policías
  await paso(page, 'Policías');
  await campos(page).nth(0).fill('PEDRO RAMIREZ LOPEZ');
  await campos(page).nth(1).fill('1000000002');
  await campos(page).nth(2).fill('PATRULLERO');
  await campos(page).nth(3).fill('3000000000');
  await arriba(page);
  await resaltar(page, etiqueta(page, /^NOMBRES Y APELLIDOS/i), 1);
  await foto(page, '07-policias');
  await quitarResaltes(page);

  // 08: Elementos incautados (se escoge 1)
  await paso(page, 'Elementos Incautados');
  await arriba(page);
  await page.getByRole('button', { name: '1', exact: true }).first().click();
  await page.waitForTimeout(600);
  await foto(page, '08-elementos');

  // 09: Hechos
  await paso(page, 'Hechos');
  await campos(page).nth(0).fill('2026-10-16');
  await campos(page).nth(1).fill('14:30');
  await campos(page).nth(2).fill('2026-10-16');
  await campos(page).nth(4).fill('Texto de ejemplo para la guia. Aqui se narra, en orden y con claridad, lo que sucedio: donde, cuando y como ocurrio la captura. Use sus propias palabras; la aplicacion no cambia lo que usted escribe.');
  await arriba(page);
  await resaltar(page, etiqueta(page, /FECHA DE LA CAPTURA/i), 1);
  await resaltar(page, etiqueta(page, /FECHA A DISPOSICIÓN DEL FISCAL/i), 2);
  await resaltar(page, etiqueta(page, /NARRACIÓN DE LOS HECHOS/i), 3);
  await foto(page, '09-hechos');
  await quitarResaltes(page);

  // 10-11: Resumen (con filas en rojo y la zona de generar documentos)
  await paso(page, 'Resumen');
  // Exacto: el párrafo de arriba también CONTIENE "(falta)", pero la celda de una fila roja es solo eso.
  const falta = page.getByText(/^\(falta\)$/).first();
  await acercar(page, falta);
  await resaltar(page, falta, 1);
  await resaltar(page, page.getByText(/Falta\s+\d+/).first(), 2);
  await foto(page, '10-resumen-revisar');
  await quitarResaltes(page);

  const abrir = page.getByRole('button', { name: /Abrir carpeta del caso/ });
  await acercar(page, abrir);
  await resaltar(page, abrir, 1);
  await resaltar(page, page.getByRole('button', { name: /FPJ-5/ }).first(), 2);
  await foto(page, '11-resumen-generar');
  await quitarResaltes(page);

  // 12: licencia
  await arriba(page);
  await page.getByRole('button', { name: /Activar licencia/i }).first().click();
  await page.waitForTimeout(800);
  const clave = page.getByPlaceholder(/clave de activación/i);
  await clave.waitFor();
  // El modal ofrece botones de plan con PRECIOS. Los precios cambian y esta guía
  // se descarga y circula meses: se reemplazan por un rótulo neutro.
  // (Son enlaces o botones según el caso: se buscan los dos.)
  const planes = page.locator('a:visible, button:visible').filter({ hasText: /^\s*(Semanal|Mensual|Estaci)/i });
  console.log('botones de plan tapados:', await planes.count());
  await planes.evaluateAll(els => els.forEach(el => { el.textContent = 'Plan disponible'; el.style.fontSize = '14px'; }));
  await resaltar(page, page.getByText(/comparte este ID con el soporte/i).locator('xpath=following-sibling::*[1]'), 1);
  await resaltar(page, clave, 2);
  await resaltar(page, page.getByRole('button', { name: 'Activar Licencia', exact: true }), 3);
  await foto(page, '12-licencia');
});
