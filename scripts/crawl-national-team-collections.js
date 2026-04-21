#!/usr/bin/env node
// One-off crawl script for Phase 2 Task 1. Fetches country collection pages,
// extracts title / meta / H1 / description / product count / schema / WC2026 mention.

const https = require('node:https');
const fs = require('node:fs');
const path = require('node:path');

const BASE = 'https://www.prosoccer.com';
const UA = 'Mozilla/5.0 (compatible; 7Rock-SEO-Audit/1.0)';

const targets = [
  '/collections/2026-fifa-world-cup',
  '/collections/mexico',
  '/collections/argentina',
  '/collections/brazil',
  '/collections/england',
  '/collections/germany',
  '/collections/france',
  '/collections/portugal',
  '/collections/spain',
  '/collections/italy',
  '/collections/netherlands',
  '/collections/south-korea',
  '/collections/guatemala',
  '/collections/el-salvador',
  '/collections/honduras',
  '/collections/colombia',
  '/collections/chile',
  '/collections/uruguay',
  '/collections/united-states-men',
  '/collections/united-states-men-women',
  '/collections/united-states-women',
  '/collections/croatia',
  '/collections/austria',
  '/collections/belgium',
  '/collections/japan',
  '/collections/canada',
  '/collections/morocco',
  '/collections/switzerland',
  '/collections/norway',
  '/collections/jamaica',
  '/collections/algeria-national-soccer-team-jerseys-apparel',
  '/collections/ghana-national-soccer-team-jerseys-apparel',
  '/collections/senegal-national-soccer-team-jerseys-apparel',
  '/collections/sweden-national-soccer-team-jerseys-apparel',
  '/collections/new-zealand-national-soccer-team-jerseys-apparel',
  '/collections/scotland-national-soccer-team-jerseys-apparel',
  '/collections/australia-national-soccer-team-jerseys-apparel',
  '/collections/usa-national-soccer-team-denim-apparel',
];

function fetch(urlPath) {
  return new Promise((resolve) => {
    const url = BASE + urlPath;
    const req = https.get(url, { headers: { 'User-Agent': UA }, timeout: 20000 }, (res) => {
      let body = '';
      res.on('data', (c) => (body += c));
      res.on('end', () => resolve({ urlPath, status: res.statusCode, headers: res.headers, body }));
    });
    req.on('error', (e) => resolve({ urlPath, status: 0, error: e.message }));
    req.on('timeout', () => { req.destroy(); resolve({ urlPath, status: 0, error: 'timeout' }); });
  });
}

function extract(html, urlPath) {
  if (!html) return { urlPath, error: 'empty body' };
  const pick = (re) => { const m = html.match(re); return m ? m[1].trim() : null; };
  const title = pick(/<title[^>]*>([^<]*)<\/title>/i);
  const metaDesc = pick(/<meta[^>]+name=["']description["'][^>]+content=["']([^"']*)["']/i)
    || pick(/<meta[^>]+content=["']([^"']*)["'][^>]+name=["']description["']/i);
  const ogTitle = pick(/<meta[^>]+property=["']og:title["'][^>]+content=["']([^"']*)["']/i);
  const ogDesc = pick(/<meta[^>]+property=["']og:description["'][^>]+content=["']([^"']*)["']/i);
  const canonical = pick(/<link[^>]+rel=["']canonical["'][^>]+href=["']([^"']*)["']/i);
  const robots = pick(/<meta[^>]+name=["']robots["'][^>]+content=["']([^"']*)["']/i);

  const h1Matches = [...html.matchAll(/<h1[^>]*>([\s\S]*?)<\/h1>/gi)].map((m) => m[1].replace(/<[^>]+>/g, '').trim()).filter(Boolean);
  const h2Matches = [...html.matchAll(/<h2[^>]*>([\s\S]*?)<\/h2>/gi)].map((m) => m[1].replace(/<[^>]+>/g, '').trim()).filter(Boolean);

  // Shopify product card count (theme-specific but common patterns)
  const productCardPatterns = [
    /class="[^"]*\bproduct-card\b[^"]*"/g,
    /class="[^"]*\bproduct-item\b[^"]*"/g,
    /class="[^"]*\bgrid__item[^"]*"\s+data-product-id/g,
    /data-product-id="/g,
    /class="[^"]*\bproduct-grid-item\b[^"]*"/g,
  ];
  const productCounts = productCardPatterns.map((re) => (html.match(re) || []).length);
  const bestProductCount = Math.max(...productCounts);

  // Pagination hints for total product count
  const pagCount = pick(/(\d+)\s*products?/i) || pick(/of\s+(\d+)\s+products/i);

  // Schema detection (LD-JSON and Microdata)
  const ldJsonBlocks = [...html.matchAll(/<script[^>]+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)].map((m) => m[1].trim());
  const schemaTypes = new Set();
  for (const block of ldJsonBlocks) {
    try {
      const parsed = JSON.parse(block);
      const items = Array.isArray(parsed) ? parsed : [parsed];
      for (const item of items) {
        if (!item) continue;
        if (item['@type']) {
          if (Array.isArray(item['@type'])) item['@type'].forEach((t) => schemaTypes.add(t));
          else schemaTypes.add(item['@type']);
        }
        if (item['@graph'] && Array.isArray(item['@graph'])) {
          for (const g of item['@graph']) if (g['@type']) schemaTypes.add(Array.isArray(g['@type']) ? g['@type'].join(',') : g['@type']);
        }
      }
    } catch { /* swallow malformed JSON-LD */ }
  }

  // WC2026 mention check
  const wcMention = /(2026\s*fifa|fifa\s*2026|world\s*cup\s*2026|2026\s*world\s*cup)/i.test(html);

  // Collection description proxy: text inside a collection description container
  const descContainer = pick(/<div[^>]+class="[^"]*collection[_-]?description[^"]*"[^>]*>([\s\S]*?)<\/div>/i);
  const descText = descContainer ? descContainer.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim() : null;

  // Breadcrumb presence
  const hasBreadcrumb = /<nav[^>]+class="[^"]*breadcrumb/i.test(html) || /itemtype="[^"]*BreadcrumbList/i.test(html);

  // Hreflang count as a locale signal
  const hreflangCount = (html.match(/<link[^>]+rel=["']alternate["'][^>]+hreflang=/gi) || []).length;

  return {
    urlPath,
    title,
    titleLen: title ? title.length : 0,
    metaDesc,
    metaDescLen: metaDesc ? metaDesc.length : 0,
    ogTitle,
    ogDesc,
    canonical,
    robots,
    h1Count: h1Matches.length,
    h1: h1Matches,
    h2Count: h2Matches.length,
    h2Sample: h2Matches.slice(0, 8),
    productCardCountDomHeuristic: bestProductCount,
    productCountInText: pagCount,
    schemaTypes: [...schemaTypes],
    wcMention,
    descText,
    hasBreadcrumb,
    hreflangCount,
  };
}

async function main() {
  const results = [];
  // Fetch in small batches of 8 to avoid slamming the origin
  for (let i = 0; i < targets.length; i += 8) {
    const batch = targets.slice(i, i + 8);
    const responses = await Promise.all(batch.map(fetch));
    for (const r of responses) {
      if (r.status === 200) results.push({ ...extract(r.body, r.urlPath), status: r.status });
      else results.push({ urlPath: r.urlPath, status: r.status, error: r.error || `HTTP ${r.status}` });
    }
  }
  const outPath = path.join(process.cwd(), 'data', 'crawl-2026-04-21_national-team-collections.json');
  fs.writeFileSync(outPath, JSON.stringify(results, null, 2));
  console.log(`Wrote ${results.length} results to ${outPath}`);
  // Terse summary
  for (const r of results) {
    if (r.error) { console.log(`${r.status || '?'}  ERROR  ${r.urlPath}  ${r.error}`); continue; }
    console.log(`200  ${r.urlPath}\n     title: ${r.title} (${r.titleLen})\n     meta:  ${(r.metaDesc || '').slice(0, 120)}${r.metaDescLen > 120 ? '…' : ''} (${r.metaDescLen})\n     h1:    ${r.h1.join(' | ')}\n     prod:  dom=${r.productCardCountDomHeuristic} text=${r.productCountInText}  WC2026=${r.wcMention}  schema=${r.schemaTypes.join(',')}`);
  }
}

main();
