// Genera los documentos REALES de la app (FPJ-5, 6, 7, 8 y acta de incautación) con un caso inventado
// y COMPLETO, para mostrarlos en la landing. Red simulada. Salida: .docx en GUIA_OUT/docs.
import { test } from '@playwright/test';
import fs from 'node:fs';
import { prepararRed, primerIngreso, OUT } from './util-guia.js';

const campos = (page) => page.locator('input:visible, textarea:visible, select:visible');
const arriba = (page) => page.evaluate(() => window.scrollTo(0, 0));
const paso = async (page, nombre) => {
  await page.getByRole('button', { name: new RegExp(`${nombre}\\s*$`) }).first().click();
  await page.waitForTimeout(600);
};

// Escribe en el control que sigue a una etiqueta. Si es un <select>, elige la opción indicada (o la primera válida).
async function poner(page, re, valor, faltan) {
  try {
    const lab = page.locator('label', { hasText: re }).first();
    if (!(await lab.count())) { faltan.push(String(re)); return; }
    const ctl = lab.locator('xpath=following::*[self::input or self::textarea or self::select][1]');
    const tag = await ctl.evaluate(e => e.tagName, null, { timeout: 4000 });
    if (tag === 'SELECT') {
      try { await ctl.selectOption({ label: valor }, { timeout: 3000 }); }
      catch { const ops = await ctl.locator('option').allTextContents(); const i = ops.findIndex((t, k) => k > 0 && t.trim()); await ctl.selectOption({ index: Math.max(i, 1) }, { timeout: 3000 }); }
    } else { await ctl.fill(valor, { timeout: 4000 }); }
  } catch (e) { faltan.push(String(re) + ' ERR ' + String(e.message).split(/\r?\n/)[0].slice(0, 80)); }
}
async function etiquetas(page) {
  return page.locator('label:visible').allTextContents().then(l => l.map(t => t.replace(/\s+/g, ' ').trim()).filter(Boolean));
}

test('documentos generados', async ({ page }) => {
  test.setTimeout(280000); page.setDefaultTimeout(10000);
  const faltan = [];
  await prepararRed(page);
  await primerIngreso(page, { capturar: false });
  await page.getByRole('button', { name: /^Captura en flagrancia/ }).click();
  await page.waitForTimeout(400);

  // Encabezado
  await paso(page, 'Encabezado');
  console.log('ETQ-ENCABEZADO', JSON.stringify(await etiquetas(page)));
  await poner(page, /^Presunto delito 1/i, 'HURTO (ART. 239 C.P.)', faltan);
  await poner(page, /^Direcci[oó]n del lugar/i, 'CARRERA 7 # 45-12', faltan);
  await poner(page, /^Barrio$/i, 'CHAPINERO', faltan);
  await poner(page, /^Localidad/i, 'CHAPINERO', faltan);

  // Capturados
  await paso(page, 'Capturados');
  const base = [[/^Primer nombre/i, 'CARLOS'], [/^Segundo nombre/i, 'ANDRES'], [/^Primer apellido/i, 'RAMIREZ'], [/^Segundo apellido/i, 'DIAZ'],
    [/^No\. documento/i, '1020345678'], [/^Fecha de nacimiento/i, '1992-03-14'], [/^Municipio de nacimiento/i, 'BOGOTA'], [/^Profesi[oó]n/i, 'COMERCIANTE'], [/^G[eé]nero/i, 'Masculino']];
  for (const [re, v] of base) await poner(page, re, v, faltan);
  console.log('ETQ-CAPTURADOS', JSON.stringify(await etiquetas(page)));
  const mapaCap = [[/^Direcci[oó]n\*/i, 'CALLE 45 # 12-30'], [/^Barrio\*/i, 'LA MACARENA'], [/^Tel[eé]fono\*/i, '3001234567'], [/^Correo electr/i, 'ejemplo@correo.com'],
    [/^Estado civil/i, 'Soltero'], [/^Se[ñn]ales/i, 'NINGUNA'], [/^Nombre del padre/i, 'JORGE RAMIREZ'], [/^Nombre de la madre/i, 'MARIA DIAZ'],
    [/^Expedido en/i, 'BOGOTA'], [/^Escolaridad/i, 'Bachiller'], [/A qui[eé]n notificar/i, 'Familiar'], [/D[oó]nde fue realizada/i, 'Lugar de los hechos']];
  for (const [re, v] of mapaCap) await poner(page, re, v, faltan);

  // Policías
  await paso(page, 'Policías');
  await campos(page).nth(0).fill('PEDRO RAMIREZ LOPEZ'); await campos(page).nth(1).fill('1000000002');
  await campos(page).nth(2).fill('PATRULLERO'); await campos(page).nth(3).fill('3000000000');

  // Elementos incautados
  await paso(page, 'Elementos Incautados');
  await arriba(page);
  await page.getByRole('button', { name: '1', exact: true }).first().click();
  await page.waitForTimeout(600);
  console.log('ETQ-ELEMENTOS', JSON.stringify(await etiquetas(page)));
  const mapaEl = [[/^Descripci[oó]n del elemento/i, 'CELULAR SAMSUNG GALAXY A14 COLOR NEGRO, PANTALLA SIN FISURAS'], [/^Cantidad/i, '1'],
    [/D[oó]nde se incaut/i, 'Capturado'], [/^Ubicaci[oó]n espec/i, 'BOLSILLO DERECHO DEL PANTALON'], [/A qui[eé]n se le encontr/i, 'Capturado'],
    [/^Hall[oó] \(H\)/i, 'PEDRO RAMIREZ LOPEZ'], [/^Recolect[oó] \(R\)/i, 'PEDRO RAMIREZ LOPEZ'], [/^Embal[oó] \(E\)/i, 'PEDRO RAMIREZ LOPEZ']];
  for (const [re, v] of mapaEl) await poner(page, re, v, faltan);

  // Hechos
  await paso(page, 'Hechos');
  console.log('ETQ-HECHOS', JSON.stringify(await etiquetas(page)));
  await poner(page, /FECHA DE LA CAPTURA/i, '2026-10-16', faltan);
  await poner(page, /HORA DE LA CAPTURA/i, '14:30', faltan);
  await poner(page, /FECHA A DISPOSICI/i, '2026-10-16', faltan);
  await poner(page, /NARRACI[OÓ]N DE LOS HECHOS/i, 'El dia 16 de octubre de 2026, siendo las 14:30 horas, en la carrera 7 con calle 45, la patrulla observo a una persona que sustrajo un telefono celular del local comercial y huyo. Se realizo el seguimiento y se le dio captura en flagrancia, se le informaron sus derechos y se le incauto el elemento, que fue embalado y rotulado.', faltan);

  // Resumen y descargas
  await paso(page, 'Resumen');
  fs.mkdirSync(`${OUT}/docs`, { recursive: true });
  const botones = [['fpj5', /FPJ-5/], ['fpj6', /FPJ-6/], ['fpj7', /FPJ-7/], ['fpj8', /FPJ-8/], ['acta', /Acta de Incautaci/]];
  for (const [nombre, re] of botones) {
    const b = page.getByRole('button', { name: re }).first();
    if (!(await b.count())) { console.log('SIN-BOTON', nombre); continue; }
    await b.scrollIntoViewIfNeeded();
    const [dl] = await Promise.all([page.waitForEvent('download', { timeout: 30000 }), b.click()]);
    await dl.saveAs(`${OUT}/docs/${nombre}.docx`);
    console.log('GENERADO', nombre, dl.suggestedFilename());
  }
  console.log('BOTONES', JSON.stringify((await page.getByRole('button').allTextContents()).map(t => t.replace(/\s+/g, ' ').trim()).filter(t => /FPJ|Acta/i.test(t))));
  console.log('NO-ENCONTRADAS', JSON.stringify(faltan));
});
