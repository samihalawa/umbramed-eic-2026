const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const screenshotDir = path.join(__dirname, 'screenshots');
if (!fs.existsSync(screenshotDir)) {
  fs.mkdirSync(screenshotDir);
}

const views = [
  { name: 'inicio', hash: '#/inicio', title: 'Inicio - Dashboard' },
  { name: 'pacientes', hash: '#/pacientes', title: 'Pacientes' },
  { name: 'recetas', hash: '#/recetas', title: 'Recetas' },
  { name: 'firma', hash: '#/firma', title: 'Firma Masiva' },
];

async function screenshot() {
  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const page = await context.newPage();

  for (const view of views) {
    const url = `file://${__dirname}/demo.html${view.hash}`;
    console.log(`📸 Capturing: ${view.title} (${url})`);

    await page.goto(url);
    await page.waitForTimeout(500); // wait for render

    const filePath = path.join(screenshotDir, `${view.name}.jpg`);
    await page.screenshot({ path: filePath, type: 'jpeg', quality: 90 });
    console.log(`✓ Saved: ${filePath}`);
  }

  await context.close();
  await browser.close();
  console.log('\n✓ All screenshots captured!');
}

screenshot().catch(console.error);
