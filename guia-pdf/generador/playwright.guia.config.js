// Config SOLO para generar las capturas de la guía (vive en una copia de origin/main,
// no en el repo real). Mismo patrón que playwright.config.js: build de producción en
// un puerto aparte, red simulada, nada toca el Worker real.
import { defineConfig } from '@playwright/test';

const PUERTO = 5179;

export default defineConfig({
  testDir: './e2e-guia',
  fullyParallel: false,
  workers: 1,
  reporter: [['list']],
  timeout: 120_000,
  use: {
    baseURL: `http://localhost:${PUERTO}`,
    channel: 'chrome',                 // el Chrome ya instalado, no descarga nada
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1.5,
    locale: 'es-CO',
    colorScheme: 'dark',
  },
  webServer: {
    command: `npm run build && npx vite preview --port ${PUERTO} --strictPort`,
    port: PUERTO,
    reuseExistingServer: false,
    timeout: 300_000,
    stdout: 'pipe',
    stderr: 'pipe',
  },
});
