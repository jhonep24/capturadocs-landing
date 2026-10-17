// Arma el PDF de la guía a partir de la maqueta (guia-print.tpl.html) y las capturas.
// Uso (desde la copia de la app): node e2e-guia/hacer-pdf.mjs <carpeta-pdf> <salida.pdf>
import { chromium } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const [carpeta, salida] = process.argv.slice(2);
if (!carpeta || !salida) { console.error('faltan argumentos'); process.exit(1); }

let html = fs.readFileSync(path.join(carpeta, 'guia-print.tpl.html'), 'utf8');

// {{img:nombre|pie}} → figura SOLO si el archivo existe en img-usuario/ (las capturas
// de Explorador, Word e impresión las toma el usuario; no se pueden generar desde la app web).
const faltan = [];
html = html.replace(/\{\{img:([a-z0-9-]+)\|([^}]*)\}\}/g, (_, nombre, pie) => {
  for (const ext of ['png', 'jpg', 'jpeg']) {
    const rel = `img-usuario/${nombre}.${ext}`;
    if (fs.existsSync(path.join(carpeta, rel))) {
      return `<figure class="chica"><img src="${rel}" alt=""/><figcaption>${pie}</figcaption></figure>`;
    }
  }
  faltan.push(nombre);
  return '';
});

const archivoHtml = path.join(carpeta, 'guia-print.html');
fs.writeFileSync(archivoHtml, html, 'utf8');

const navegador = await chromium.launch({ channel: 'chrome' });
const pagina = await navegador.newPage();
await pagina.goto(pathToFileURL(archivoHtml).href, { waitUntil: 'load' });
await pagina.emulateMedia({ media: 'print' });
await pagina.pdf({
  path: salida,
  format: 'A4',
  printBackground: true,
  displayHeaderFooter: true,
  headerTemplate: '<span></span>',
  footerTemplate: `<div style="width:100%;font-size:8px;color:#6b7893;font-family:Segoe UI,Arial,sans-serif;padding:0 15mm;display:flex;justify-content:space-between"><span>CapturaDocs Express · Guía paso a paso</span><span>Página <span class="pageNumber"></span> de <span class="totalPages"></span></span></div>`,
  margin: { top: '16mm', bottom: '18mm', left: '15mm', right: '15mm' },
});
await navegador.close();

console.log('PDF:', salida, Math.round(fs.statSync(salida).size / 1024), 'KB');
if (faltan.length) console.log('Imágenes del usuario que faltan (la guía sale sin ellas):', faltan.join(', '));
