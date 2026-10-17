// Utilidades compartidas de las capturas de la guía.
import { aislarRed } from '../e2e/utilidades.js';

export const OUT = process.env.GUIA_OUT;

export const ESTADO_TRIAL = {
  status: 'trial', trial: true, deviceId: 'B57F-E64B',
  trialUsed: 0, trialTotal: 5, trialLeft: 5, iaAllowed: false,
  cfg: { whatsapp: '3503593635', nequi: '3503593635' },
};

// Datos 100% inventados para que la guía pública no muestre nada real.
export const FICTICIO = {
  correo: 'ejemplo@correo.com',
  nunc: '110016000000202600001',
  departamento: 'CUNDINAMARCA',
  municipio: 'BOGOTA',
  destino: 'URI DE EJEMPLO',
};

export async function prepararRed(page, estado = ESTADO_TRIAL) {
  // La app pregunta window.electronAPI para decidir si muestra el botón
  // "Abrir carpeta del caso" (solo existe en la app instalada de Windows).
  // Se declara aquí para que la captura muestre la pantalla REAL de esa app.
  await page.addInitScript(() => {
    window.electronAPI = {
      abrirDescargas: async () => {},
      obtenerMachineId: async () => null,
      setCarpetaCaso: async () => {},
    };
  });
  return aislarRed(page, estado);
}

// Pone un borde + número sobre un elemento, para señalar dónde hacer clic.
// Se ancla a coordenadas del DOCUMENTO (no de la ventana) y NO mueve la
// página: así varios resaltes en la misma pantalla no se descuadran entre sí.
// Si el elemento está fuera de la pantalla visible, antes hay que acercarlo
// con `acercar()`.
export async function resaltar(page, locator, numero) {
  const handle = await locator.first().elementHandle();
  await page.evaluate(([el, n]) => {
    const r = el.getBoundingClientRect();
    const x = r.left + window.scrollX, y = r.top + window.scrollY;
    const caja = document.createElement('div');
    caja.className = '__resalte';
    caja.style.cssText = `position:absolute;left:${x - 6}px;top:${y - 6}px;width:${r.width + 12}px;height:${r.height + 12}px;border:3px solid #ff5a36;border-radius:10px;box-shadow:0 0 0 4px rgba(255,90,54,.25);pointer-events:none;z-index:99999`;
    if (n) {
      const b = document.createElement('div');
      b.textContent = n;
      b.style.cssText = 'position:absolute;left:-14px;top:-14px;width:28px;height:28px;border-radius:50%;background:#ff5a36;color:#fff;font:700 16px system-ui;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 6px rgba(0,0,0,.4)';
      caja.appendChild(b);
    }
    document.body.appendChild(caja);
  }, [handle, numero]);
}

// Acerca un elemento al centro de la pantalla ANTES de poner los resaltes.
export async function acercar(page, locator) {
  await locator.first().evaluate(el => el.scrollIntoView({ block: 'center' }));
  await page.waitForTimeout(250);
}

export async function quitarResaltes(page) {
  await page.evaluate(() => document.querySelectorAll('.__resalte').forEach(e => e.remove()));
}

export async function foto(page, nombre) {
  await page.waitForTimeout(350);
  await page.screenshot({ path: `${OUT}/${nombre}.png` });
}

// Términos → correo → configuración inicial (con datos inventados).
export async function primerIngreso(page, { capturar = false } = {}) {
  await page.goto('/');
  const casilla = page.getByRole('checkbox').first();
  await casilla.waitFor();
  const aceptar = page.getByRole('button', { name: /Aceptar y continuar/i });
  if (capturar) await foto(page, '01-terminos');
  await casilla.check();
  if (capturar) {
    await acercar(page, aceptar);
    await resaltar(page, casilla, 1);
    await resaltar(page, aceptar, 2);
    await foto(page, '01b-terminos-marcado');
    await quitarResaltes(page);
  }
  await aceptar.click();

  const emails = page.locator('input[type="email"]');
  await emails.nth(0).waitFor();
  await emails.nth(0).fill(FICTICIO.correo);
  await emails.nth(1).fill(FICTICIO.correo);
  const continuar = page.getByRole('button', { name: /Continuar/i });
  if (capturar) {
    await resaltar(page, emails.nth(0), 1);
    await resaltar(page, emails.nth(1), 2);
    await resaltar(page, page.getByPlaceholder(/REF-/), 3);
    await resaltar(page, continuar, 4);
    await foto(page, '02-registro-correo');
    await quitarResaltes(page);
  }
  await continuar.click();

  // Configuración inicial: viene precargada con valores por defecto de la app;
  // se reemplazan por inventados antes de cualquier captura.
  await page.locator('input:visible').nth(0).waitFor();
  const campos = [FICTICIO.nunc, FICTICIO.departamento, FICTICIO.municipio, FICTICIO.destino];
  for (let i = 0; i < 4; i++) await page.locator('input:visible').nth(i).fill(campos[i]);
  const guardar = page.getByRole('button', { name: /Guardar y continuar/i });
  if (capturar) {
    await resaltar(page, guardar, 1);
    await foto(page, '03-configuracion-inicial');
    await quitarResaltes(page);
  }
  await guardar.click();
  await page.waitForTimeout(1500);
}
