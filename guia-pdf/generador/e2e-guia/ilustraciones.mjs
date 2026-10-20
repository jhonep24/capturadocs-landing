// Dibuja las 3 ilustraciones (Explorador, Word, impresión) desde generador/ilustraciones/*.html.
// Uso (con @playwright/test disponible): node ilustraciones.mjs <carpeta-ilustraciones> <carpeta-salida>
import { chromium } from '@playwright/test';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
const [src, out] = process.argv.slice(2);
const nav = await chromium.launch({ channel: 'chrome' });
for (const n of ['explorador', 'word-pdf', 'imprimir-escala']) {
  const p = await nav.newPage({ viewport: { width: 932, height: 600 }, deviceScaleFactor: 2 });
  await p.goto(pathToFileURL(path.join(src, n + '.html')).href);
  await p.screenshot({ path: path.join(out, n + '.png'), fullPage: true });
}
await nav.close();
