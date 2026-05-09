"""Classify the 1,000 GSC-exported 404 URLs into systemic patterns vs one-off redirects.

Inputs:
  - data/gsc-exports/2026-05-08_404-table.csv (URL, Last crawled)
  - deliverables/tracking/sitemap-state.md (canonical-URL inventory)
  - 90-day GSC page-level impressions data (already pulled — used to assign priority)

Outputs:
  - data/gsc-exports/2026-05-08_404-classified.csv (URL, classification, suggested_target, priority)
  - data/gsc-exports/2026-05-08_404-systemic-summary.txt (systemic-pattern counts)

Run from repo root: python scripts/_classify_404_table.py
"""

from __future__ import annotations

import csv
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

REPO = Path(__file__).resolve().parents[1]
INPUT_404 = REPO / "data" / "gsc-exports" / "2026-05-08_404-table.csv"
SITEMAP_STATE = REPO / "deliverables" / "tracking" / "sitemap-state.md"
OUT_CLASSIFIED = REPO / "data" / "gsc-exports" / "2026-05-08_404-classified.csv"
OUT_SUMMARY = REPO / "data" / "gsc-exports" / "2026-05-08_404-systemic-summary.txt"

GSC_TOOL_RESULTS = [
    Path(r"C:\Users\Ashot\.claude\projects\C--Dev-Projects-marketing-prosoccer-seo\fd38fafa-7bb8-4815-9ef2-a5c91d6db935\tool-results\mcp-gsc-server-get_advanced_search_analytics-1778283836917.txt"),
    Path(r"C:\Users\Ashot\.claude\projects\C--Dev-Projects-marketing-prosoccer-seo\fd38fafa-7bb8-4815-9ef2-a5c91d6db935\tool-results\mcp-gsc-server-get_advanced_search_analytics-1778284117718.txt"),
]

PRODUCT_SITEMAP_CHUNKS = [
    "https://www.prosoccer.com/sitemap_products_1.xml?from=7629581353215&to=7631474163967",
    "https://www.prosoccer.com/sitemap_products_2.xml?from=7631474229503&to=7731099173119",
    "https://www.prosoccer.com/sitemap_products_3.xml?from=7731101958399&to=8056578507007",
    "https://www.prosoccer.com/sitemap_products_4.xml?from=8056581423359&to=8758357885183",
    "https://www.prosoccer.com/sitemap_products_5.xml?from=8758362210559&to=9147497087231",
    "https://www.prosoccer.com/sitemap_products_6.xml?from=9147693433087&to=9444442276095",
    "https://www.prosoccer.com/sitemap_products_7.xml?from=9444445421823&to=9490182340863",
]


def load_sitemap_paths() -> set[str]:
    paths: set[str] = set()
    text = SITEMAP_STATE.read_text(encoding="utf-8")
    for line in text.splitlines():
        m = re.match(r"^(/(collections|pages|blogs)/[^\s`]+)", line.strip())
        if m:
            paths.add(m.group(1))
    paths.update({"/", "/agents.md", "/llms-full.txt", "/llms.txt"})
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    for chunk_url in PRODUCT_SITEMAP_CHUNKS:
        try:
            with urllib.request.urlopen(chunk_url, timeout=30) as resp:
                data = resp.read()
        except Exception as exc:
            print(f"  WARN: could not fetch {chunk_url}: {exc}", file=sys.stderr)
            continue
        root = ET.fromstring(data)
        for url_elem in root.findall("sm:url/sm:loc", ns):
            loc = (url_elem.text or "").strip()
            parsed = urlparse(loc)
            if parsed.netloc.endswith("prosoccer.com") and parsed.path.startswith("/products/"):
                paths.add(parsed.path.rstrip("/"))
    return paths


def load_impressions_index() -> dict[str, tuple[int, int]]:
    """url_path_with_query -> (clicks, impressions) over 90 days."""
    idx: dict[str, tuple[int, int]] = {}
    for path in GSC_TOOL_RESULTS:
        if not path.exists():
            continue
        outer = json.loads(path.read_text(encoding="utf-8"))
        inner = json.loads(outer["result"])
        for r in inner.get("rows", []):
            url = r.get("page")
            if not url:
                continue
            parsed = urlparse(url)
            key = parsed.path + (("?" + parsed.query) if parsed.query else "")
            clicks = int(r.get("clicks", 0) or 0)
            impressions = int(r.get("impressions", 0) or 0)
            prev = idx.get(key, (0, 0))
            idx[key] = (max(prev[0], clicks), max(prev[1], impressions))
    return idx


# Systemic patterns -- anchored on URL path, not host
RE_ES_LOCALE = re.compile(r"^/(es|es-es|es-mx|es-co)(/|$)")
RE_DUPLICATED_LOCALE = re.compile(r"^/(en-[a-z]{2})/\1/")
RE_DISCOVERY_PARAM = re.compile(r"_rdiscovery-(handle|widget|product)")
RE_LOCALE_PREFIX = re.compile(r"^/(en-[a-z]{2})/")
RE_NUMERIC_PRODUCT = re.compile(r"^/products/\d{6,}/?$")
RE_ASSET_TEMPLATE_VAR = re.compile(r"%7B[^%]+%7D")  # {var} URL-encoded
RE_BLOG_DUP_SEGMENT = re.compile(r"^/blogs/([^/]+)/\1/")
RE_VARIANT_PARAM = re.compile(r"(^|&)variant=\d+")
RE_NAME_SET = re.compile(r"(name-set|name-and-number|customization-template|-blank-)")
RE_PAGE_PARAM = re.compile(r"(^|&)page=\d+")
RE_FILTER_PARAM = re.compile(r"(^|&)filter\.")
RE_VIDEO_STREAM = re.compile(
    r"^(/content/stream/|/v/media/storage/|/static/uploads/v/|/assets/content/v/|/upload/media/video/|/media/mp4/|/assets/video/|/assets/mp4/v/|/public/video/)"
)
RE_VIDEO_ONLINES = re.compile(r"\.mp4/onlines/")
RE_PLAYER_QUERY = re.compile(r"^/player$")
RE_WPM_SANDBOX = re.compile(r"^/wpm@")
RE_MAGENTO_LEGACY = re.compile(
    r"^/(customer/account/|catalog/product/|catalog/category/|catalog/product_compare/|checkout/cart|sales/|admin/|wishlist/index/|review/product/list/|customer/section/load/)"
)
RE_ENCODED_HANDLE = re.compile(r"�")  # Unicode replacement char in handle
RE_TYPES_COLLECTION = re.compile(r"^/collections/types$")


def classify(url: str, sitemap: set[str]) -> tuple[str, str]:
    """Return (classification_bucket, suggested_target_or_note)."""
    parsed = urlparse(url)
    path = parsed.path
    query = parsed.query
    full_path_q = path + (("?" + query) if query else "")

    # Asset URLs with unsubstituted template variables
    if RE_ASSET_TEMPLATE_VAR.search(full_path_q):
        return ("systemic-asset-template-var", "theme template variable not substituted")

    # Video stream URLs (third-party video app) -- .mp4 path or .mp4/onlines/ subpath
    if (RE_VIDEO_STREAM.match(path) and path.endswith(".mp4")) or RE_VIDEO_ONLINES.search(path):
        return ("systemic-video-stream-app", "video app generating non-resolving stream URLs")

    # /player?id=X video player query
    if RE_PLAYER_QUERY.match(path):
        return ("systemic-video-stream-app", "video app /player query URL")

    # Encoded/replacement-char in product handle (mangled inbound link)
    if RE_ENCODED_HANDLE.search(path):
        return ("systemic-encoded-handle", "URL contains replacement char; mangled inbound link")

    # Shopify Web Pixel Manager sandbox URLs (should never be indexed)
    if RE_WPM_SANDBOX.match(path):
        return ("systemic-wpm-sandbox", "Web Pixel Manager sandbox URL; needs robots.txt block")

    # Magento legacy URLs (customer/account/, catalog/, etc.)
    if RE_MAGENTO_LEGACY.match(path):
        return ("systemic-magento-legacy", "Magento 1 legacy URL pattern")

    # /collections/types (single non-existent collection with many ?page=N variants)
    if RE_TYPES_COLLECTION.match(path):
        return ("systemic-types-collection", "non-existent /collections/types; remove or 410")

    # /es/, /es-es/, etc. (non-canonical Spanish locale paths)
    if RE_ES_LOCALE.match(path):
        return ("systemic-es-locale", "non-canonical Spanish locale routing")

    # Duplicated locale prefix /en-au/en-au/...
    if RE_DUPLICATED_LOCALE.match(path):
        return ("systemic-duplicated-locale", "locale prefix duplicated by routing")

    # Rebuy Discovery widget links with locale prefix
    if RE_LOCALE_PREFIX.match(path) and RE_DISCOVERY_PARAM.search(query or ""):
        return ("systemic-locale-discovery-widget", "Rebuy widget URL on locale path")

    # Other locale-prefixed 404s (en-XX without discovery)
    if RE_LOCALE_PREFIX.match(path):
        return ("systemic-locale-other", "locale-prefixed 404; route to VERITAS hreflang work")

    # Discovery widget on canonical path (variant + _rdiscovery)
    if RE_DISCOVERY_PARAM.search(query or ""):
        return ("systemic-discovery-widget", "Rebuy widget URL")

    # Numeric Shopify product IDs
    if RE_NUMERIC_PRODUCT.match(path):
        return ("systemic-numeric-product-id", "Shopify product ID URL; needs handle redirect")

    # Blog with duplicated segment
    if RE_BLOG_DUP_SEGMENT.match(path):
        m = RE_BLOG_DUP_SEGMENT.match(path)
        rest = path[len(m.group(0)) :]
        canonical = f"/blogs/{m.group(1)}/{rest}"
        return ("systemic-blog-duplicated-path", canonical)

    # Name Set products (excluded per prior agency configuration)
    if RE_NAME_SET.search(path):
        return ("excluded-name-set", "intentionally noindexed by prior agency")

    # Pagination ?page=N
    if RE_PAGE_PARAM.search(query or ""):
        return ("systemic-pagination", "deep-pagination 404; canonical fix")

    # Filter parameter URLs
    if RE_FILTER_PARAM.search(query or ""):
        return ("systemic-filter-param", "filter parameter URL")

    # Variant param on canonical product
    if RE_VARIANT_PARAM.search(query or ""):
        if path.startswith("/products/"):
            base = path.rstrip("/")
            if base in sitemap:
                return ("systemic-variant-on-live-product", base)
            return ("systemic-variant-on-dead-product", "underlying product handle missing")
        if "/products/" in path:
            handle = "/products/" + path.split("/products/", 1)[1].rstrip("/")
            if handle in sitemap:
                return ("systemic-nested-variant-canonical", handle)
            return ("one-off-nested-variant-dead", "underlying handle missing")

    # Nested collection-product without variant param
    if "/collections/" in path and "/products/" in path:
        handle = "/products/" + path.split("/products/", 1)[1].rstrip("/")
        if handle in sitemap:
            return ("systemic-nested-collection-product", handle)
        return ("one-off-nested-product-dead", "underlying handle missing; needs lookup")

    # One-off product 404
    if path.startswith("/products/"):
        return ("one-off-product-404", "needs handle correction or 410")

    # One-off collection 404
    if path.startswith("/collections/"):
        return ("one-off-collection-404", "needs collection redirect or 410")

    # One-off page 404
    if path.startswith("/pages/"):
        return ("one-off-page-404", "needs page redirect or 410")

    # One-off blog 404
    if path.startswith("/blogs/"):
        return ("one-off-blog-404", "needs blog redirect or 410")

    # Bare .html legacy
    if path.endswith(".html"):
        return ("one-off-legacy-html", "Magento-era URL pattern; verify and redirect")

    return ("one-off-other", "manual review")


def suggest_target_from_typo(handle: str, sitemap: set[str]) -> str | None:
    """Try to find a close handle in sitemap for a typo'd product handle."""
    target_candidates = [p for p in sitemap if p.startswith("/products/")]
    handle_part = handle.replace("/products/", "")
    # Try common typo fixes
    fixes = {
        "addias": "adidas",
        "adiads": "adidas",
        "nikee": "nike",
        "puuma": "puma",
    }
    for typo, fix in fixes.items():
        if typo in handle_part:
            candidate = f"/products/{handle_part.replace(typo, fix)}"
            if candidate in sitemap:
                return candidate
    return None


def main() -> None:
    print("Loading sitemap")
    sitemap = load_sitemap_paths()
    print(f"  {len(sitemap)} canonical paths")

    print("Loading 90-day impressions index")
    imps = load_impressions_index()
    print(f"  {len(imps)} URL impressions records")

    print(f"Reading {INPUT_404}")
    rows = []
    with INPUT_404.open(encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for r in reader:
            rows.append(r)
    print(f"  {len(rows)} 404 URLs")

    classified: list[dict] = []
    bucket_counts: Counter[str] = Counter()

    for r in rows:
        url = r["URL"].strip()
        last_crawled = r.get("Last crawled", "").strip()
        bucket, target = classify(url, sitemap)
        bucket_counts[bucket] += 1

        # Try typo fix for one-off product 404s
        if bucket == "one-off-product-404":
            parsed = urlparse(url)
            fix = suggest_target_from_typo(parsed.path, sitemap)
            if fix:
                target = fix

        # Priority from impressions data
        parsed = urlparse(url)
        key = parsed.path + (("?" + parsed.query) if parsed.query else "")
        clicks, impressions = imps.get(key, (0, 0))
        if clicks > 0:
            priority = "High"
        elif impressions > 100:
            priority = "Medium"
        elif impressions > 0:
            priority = "Low"
        else:
            priority = "None"

        classified.append(
            {
                "url": url,
                "last_crawled": last_crawled,
                "bucket": bucket,
                "suggested_target_or_note": target,
                "clicks_90d": clicks,
                "impressions_90d": impressions,
                "priority": priority,
            }
        )

    OUT_CLASSIFIED.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CLASSIFIED.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "url",
                "last_crawled",
                "bucket",
                "suggested_target_or_note",
                "clicks_90d",
                "impressions_90d",
                "priority",
            ],
        )
        w.writeheader()
        w.writerows(classified)
    print(f"Wrote {OUT_CLASSIFIED}")

    # Build summary
    systemic_buckets = [b for b in bucket_counts if b.startswith("systemic-")]
    one_off_buckets = [b for b in bucket_counts if b.startswith("one-off-")]
    excluded_buckets = [b for b in bucket_counts if b.startswith("excluded-")]

    systemic_total = sum(bucket_counts[b] for b in systemic_buckets)
    one_off_total = sum(bucket_counts[b] for b in one_off_buckets)
    excluded_total = sum(bucket_counts[b] for b in excluded_buckets)

    lines = [
        f"GSC 404-table classification (sample = {len(rows)}; full set ~13K-14K per Chart)",
        "",
        f"Systemic (group, don't list individually): {systemic_total} ({systemic_total/len(rows):.1%})",
    ]
    for b in sorted(systemic_buckets, key=lambda x: -bucket_counts[x]):
        lines.append(f"  {b:42s} {bucket_counts[b]:>4d}")
    lines.append("")
    lines.append(f"One-off (individual redirects): {one_off_total} ({one_off_total/len(rows):.1%})")
    for b in sorted(one_off_buckets, key=lambda x: -bucket_counts[x]):
        lines.append(f"  {b:42s} {bucket_counts[b]:>4d}")
    lines.append("")
    lines.append(f"Excluded (Name Set / intentional): {excluded_total}")
    for b in sorted(excluded_buckets, key=lambda x: -bucket_counts[x]):
        lines.append(f"  {b:42s} {bucket_counts[b]:>4d}")
    lines.append("")

    # Priority breakdown of one-offs (the actual redirect map size)
    one_off_rows = [c for c in classified if c["bucket"].startswith("one-off-")]
    pri = Counter(c["priority"] for c in one_off_rows)
    lines.append("One-off priority breakdown (drives redirect map size):")
    for p in ["High", "Medium", "Low", "None"]:
        lines.append(f"  {p:8s} {pri.get(p, 0):>4d}")
    lines.append("")

    # High-impact one-offs sample
    high_priority = [c for c in one_off_rows if c["priority"] in ("High", "Medium")]
    lines.append(f"High/Medium priority one-offs (top 20 by impressions):")
    high_priority.sort(key=lambda c: (-c["clicks_90d"], -c["impressions_90d"]))
    for c in high_priority[:20]:
        lines.append(
            f"  {c['clicks_90d']:>3}c {c['impressions_90d']:>5}i  {c['bucket']:30s} {c['url']}"
        )

    OUT_SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
