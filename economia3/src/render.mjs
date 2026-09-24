// Imprime un HTML a PDF con Chromium (playwright-core).
// Uso: node render.mjs <entrada.html> <salida.pdf>
import { chromium } from 'playwright-core';
import { pathToFileURL } from 'node:url';
import fs from 'node:fs';
import path from 'node:path';

const [, , input, output] = process.argv;
if (!input || !output) {
  console.error('Uso: node render.mjs <entrada.html> <salida.pdf>');
  process.exit(2);
}

const candidates = [
  process.env.CHROMIUM_PATH,
  '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
].filter(Boolean);
const executablePath = candidates.find((p) => fs.existsSync(p));

const browser = await chromium.launch({ executablePath, args: ['--allow-file-access-from-files'] });
const page = await browser.newPage();
const problems = [];
page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') problems.push(`[${m.type()}] ${m.text()}`); });
page.on('pageerror', (e) => problems.push(`[pageerror] ${e.message}`));
page.on('requestfailed', (r) => problems.push(`[requestfailed] ${r.url()}`));

await page.goto(pathToFileURL(path.resolve(input)).href, { waitUntil: 'load' });
await page.waitForFunction(() => window.__READY === true, null, { timeout: 120000 });
await page.evaluate(() => document.fonts.ready);

const report = await page.evaluate(() => window.__REPORT || {});
await page.pdf({
  path: output,
  preferCSSPageSize: true,
  printBackground: true,
  outline: true,
  tagged: true,
});
await browser.close();

fs.writeFileSync(output.replace(/\.pdf$/, '.render.json'), JSON.stringify({ problems, report }, null, 2));
if (problems.length) console.error(problems.join('\n'));
console.log(`OK ${output}`);
