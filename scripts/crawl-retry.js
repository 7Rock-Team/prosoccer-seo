#!/usr/bin/env node
const https = require('node:https');
const fs = require('node:fs');
const path = require('node:path');

const BASE = 'https://www.prosoccer.com';
const UA = 'Mozilla/5.0 (compatible; 7Rock-SEO-Audit/1.0)';

const retry = [
  '/collections/chile',
  '/collections/uruguay',
  '/collections/united-states-men',
  '/collections/united-states-men-women',
  '/collections/united-states-women',
  '/collections/croatia',
  '/collections/austria',
  '/collections/belgium',
];

function fetch(urlPath) {
  return new Promise((resolve) => {
    const url = BASE + urlPath;
    const req = https.get(url, { headers: { 'User-Agent': UA }, timeout: 20000 }, (res) => {
      let body = '';
      res.on('data', (c) => (body += c));
      res.on('end', () => resolve({ urlPath, status: res.statusCode, body }));
    });
    req.on('error', (e) => resolve({ urlPath, status: 0, error: e.message }));
    req.on('timeout', () => { req.destroy(); resolve({ urlPath, status: 0, error: 'timeout' }); });
  });
}

function sleep(ms) { return new Promise((r) => setTimeout(r, ms)); }

function extract(html, urlPath) {
  const pick = (re) => { const m = html.match(re); return m ? m[1].trim() : null; };
  const title = pick(/<title[^>]*>([^<]*)<\/title>/i);
  const metaDesc = pick(/<meta[^>]+name=["']description["'][^>]+content=["']([^"']*)["']/i)
    || pick(/<meta[^>]+content=["']([^"']*)["'][^>]+name=["']description["']/i);
  const canonical = pick(/<link[^>]+rel=["']canonical["'][^>]+href=["']([^"']*)["']/i);
  const robots = pick(/<meta[^>]+name=["']robots["'][^>]+content=["']([^"']*)["']/i);
  const h1 = [...html.matchAll(/<h1[^>]*>([\s\S]*?)<\/h1>/gi)].map((m) => m[1].replace(/<[^>]+>/g, '').trim()).filter(Boolean);
  const productCards = (html.match(/class="[^"]*\bproduct-card\b[^"]*"/g) || []).length;
  const productItems = (html.match(/class="[^"]*\bproduct-item\b[^"]*"/g) || []).length;
  const dataProd = (html.match(/data-product-id="/g) || []).length;
  const bestProductCount = Math.max(productCards, productItems, dataProd);
  const ldJsonBlocks = [...html.matchAll(/<script[^>]+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)].map((m) => m[1].trim());
  const schemaTypes = new Set();
  for (const block of ldJsonBlocks) {
    try {
      const parsed = JSON.parse(block);
      const items = Array.isArray(parsed) ? parsed : [parsed];
      for (const item of items) {
        if (item && item['@type']) schemaTypes.add(Array.isArray(item['@type']) ? item['@type'].join(',') : item['@type']);
      }
    } catch {}
  }
  const wcMention = /(2026\s*fifa|fifa\s*2026|world\s*cup\s*2026|2026\s*world\s*cup)/i.test(html);
  return { urlPath, title, titleLen: title ? title.length : 0, metaDesc, metaDescLen: metaDesc ? metaDesc.length : 0, canonical, robots, h1, productCardCountDomHeuristic: bestProductCount, schemaTypes: [...schemaTypes], wcMention };
}

async function main() {
  const results = [];
  for (const urlPath of retry) {
    const r = await fetch(urlPath);
    if (r.status === 200) results.push({ ...extract(r.body, urlPath), status: 200 });
    else results.push({ urlPath, status: r.status, error: r.error || `HTTP ${r.status}` });
    await sleep(2500); // 2.5 second spacing to avoid 429
  }
  const outPath = path.join(process.cwd(), 'data', 'crawl-2026-04-21_national-team-collections-retry.json');
  fs.writeFileSync(outPath, JSON.stringify(results, null, 2));
  console.log(`Wrote ${results.length} results to ${outPath}`);
  for (const r of results) {
    if (r.error) { console.log(`${r.status || '?'}  ERROR  ${r.urlPath}  ${r.error}`); continue; }
    console.log(`200  ${r.urlPath}\n     title: ${r.title} (${r.titleLen})\n     meta:  ${(r.metaDesc || '').slice(0, 120)}${r.metaDescLen > 120 ? '…' : ''} (${r.metaDescLen})\n     h1:    ${r.h1.join(' | ')}\n     prod:  dom=${r.productCardCountDomHeuristic}  WC2026=${r.wcMention}  schema=${r.schemaTypes.join(',')}`);
  }
}

main();
