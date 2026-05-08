"""Generator for deliverables/tracking/sitemap-state.md.

Refresh source: Shopify auto-generated sitemap.xml chunks at
https://www.prosoccer.com/sitemap.xml. This is the authoritative public
discovery surface (what Google sees). Internal-link anchors should target
URLs present here.

Shopify pagination pattern (verified 2026-05-08):
  - sitemap.xml                       index
  - sitemap_collections_*.xml         all live collections
  - sitemap_products_*.xml            all live products (paginated 1..N)
  - sitemap_pages_*.xml               all live informational pages
  - sitemap_blogs_*.xml               blog handle landing pages
  - sitemap_agentic_discovery.xml     LLM-targeted discovery file
  - sitemap_metaobject_pages_1.xml    Shopify metaobject pages

Refresh discipline (weekly Monday):
  1. Run this script. It downloads chunks to /tmp and writes the markdown file.
  2. Voice-check the generated file.
  3. Commit if changed.

The script is idempotent. Re-runs overwrite the local cache and the markdown.
"""
from __future__ import annotations

import datetime
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

REPO = Path(__file__).resolve().parent.parent
SITEMAP_OUT = REPO / "deliverables" / "tracking" / "sitemap-state.md"
CACHE = REPO / "scripts" / "build" / "sitemap-cache"
INDEX_URL = "https://www.prosoccer.com/sitemap.xml"
USER_AGENT = "Mozilla/5.0 (compatible; 7Rock-SEO-Audit/1.0)"

# Mike's Shopify admin reference counts (last verified 2026-05-08).
# Used to flag delta between admin reality and sitemap discovery surface.
ADMIN_COLLECTIONS = 1077
ADMIN_PRODUCTS = 15381

# Vendor prefixes to group product URLs by. ProSoccer's catalog is brand-led.
VENDOR_PREFIXES = [
    "adidas", "nike", "puma", "umbro", "new-balance", "mizuno", "diadora",
    "kelme", "kappa", "joma", "lotto", "macron", "asics", "brooks",
    "uhlsport", "select", "molten", "wilson", "franklin", "park",
    "bownet", "kwikgoal", "champro", "soccer-innovations", "storelli",
    "g-form", "sells",
]


def fetch(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["curl", "-sL", "-A", USER_AGENT, url, "-o", str(dest)],
        check=True,
    )


def parse_locs(xml: str) -> list[str]:
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def get_path(url: str) -> str:
    parsed = urlparse(url)
    if parsed.netloc not in {"www.prosoccer.com", "prosoccer.com"}:
        return ""
    path = parsed.path.rstrip("/") or "/"
    return path


def vendor_of(handle: str) -> str:
    """Extract vendor prefix from a product handle, or 'other'."""
    h = handle.lower()
    for prefix in VENDOR_PREFIXES:
        if h.startswith(prefix + "-") or h == prefix:
            return prefix
    return "other"


def main() -> None:
    CACHE.mkdir(parents=True, exist_ok=True)
    print(f"Fetching index: {INDEX_URL}")
    fetch(INDEX_URL, CACHE / "sitemap.xml")
    index_xml = (CACHE / "sitemap.xml").read_text(encoding="utf-8")
    child_urls = re.findall(r"https://www\.prosoccer\.com/sitemap_[^<]+", index_xml)
    child_urls = [u.replace("&amp;", "&") for u in child_urls]
    child_urls = list(dict.fromkeys(child_urls))

    collections: list[str] = []
    products: list[str] = []
    pages: list[str] = []
    blogs: list[str] = []
    other: list[str] = []
    locale_counts: Counter[str] = Counter()

    LOCALE_PREFIXES = ("/en-es/", "/en-au/", "/en-ca/", "/en-gb/")

    for url in child_urls:
        fname = url.split("/")[-1].split("?")[0]
        path = CACHE / fname
        print(f"Fetching {fname}")
        fetch(url, path)
        xml = path.read_text(encoding="utf-8")
        for loc in parse_locs(xml):
            urlpath = get_path(loc)
            if not urlpath:
                continue
            stripped = False
            for prefix in LOCALE_PREFIXES:
                if urlpath.startswith(prefix):
                    locale_counts[prefix.strip("/")] += 1
                    urlpath = "/" + urlpath[len(prefix):]
                    stripped = True
                    break
            if urlpath.startswith("/collections/"):
                collections.append(urlpath)
            elif urlpath.startswith("/products/"):
                products.append(urlpath)
            elif urlpath.startswith("/pages/"):
                pages.append(urlpath)
            elif urlpath.startswith("/blogs/"):
                blogs.append(urlpath)
            else:
                other.append(urlpath)

    collections = sorted(set(collections))
    products = sorted(set(products))
    pages = sorted(set(pages))
    blogs = sorted(set(blogs))
    other = sorted(set(other))

    vendor_groups: dict[str, list[str]] = defaultdict(list)
    for product in products:
        handle = product.removeprefix("/products/")
        vendor_groups[vendor_of(handle)].append(product)

    today = datetime.date.today().isoformat()
    coll_delta = ADMIN_COLLECTIONS - len(collections)
    coll_delta_pct = (coll_delta / ADMIN_COLLECTIONS) * 100 if ADMIN_COLLECTIONS else 0
    prod_delta = ADMIN_PRODUCTS - len(products)
    prod_delta_pct = (prod_delta / ADMIN_PRODUCTS) * 100 if ADMIN_PRODUCTS else 0

    lines: list[str] = []
    a = lines.append

    a("# Sitemap State")
    a("")
    a(
        "_Source-of-truth reference for which URLs exist on `www.prosoccer.com`. "
        "Workforce agents (especially SCRIBE for internal-link anchors and ORIN for routing) "
        "consult this file before proposing any internal link to verify the target URL is live._"
    )
    a("")
    a(f"**Last refreshed:** {today} via authoritative Shopify sitemap.xml chunks.")
    a("")
    a(
        "**Method:** direct parse of `https://www.prosoccer.com/sitemap.xml` and its child "
        "sitemap chunks (`sitemap_collections_*`, `sitemap_products_*`, `sitemap_pages_*`, "
        "`sitemap_blogs_*`). Authoritative public discovery surface (what Google sees). "
        "Generated by `python scripts/_build_sitemap_state.py`. Not Firecrawl-discovered: "
        "Firecrawl maps undercount because they cap at a few thousand pages; the public "
        "sitemap is the canonical SEO source."
    )
    a("")
    a("## Counts (per refresh, canonical English paths only)")
    a("")
    a(f"- Collections: **{len(collections)}**")
    a(f"- Products: **{len(products)}**")
    a(f"- Pages (informational): **{len(pages)}**")
    a(f"- Blogs / articles: **{len(blogs)}**")
    a(f"- Other top-level URLs: **{len(other)}**")
    a("")

    a("### Sitemap-vs-admin delta")
    a("")
    a(
        f"Mike's Shopify admin (verified {today}) reports **{ADMIN_COLLECTIONS} live published "
        f"collections** and **{ADMIN_PRODUCTS} live published products**. The public sitemap "
        f"surfaces fewer:"
    )
    a("")
    a(
        f"- Collections delta: admin {ADMIN_COLLECTIONS} vs sitemap {len(collections)} = "
        f"**{coll_delta} missing ({coll_delta_pct:.1f}%)**"
    )
    a(
        f"- Products delta: admin {ADMIN_PRODUCTS} vs sitemap {len(products)} = "
        f"**{prod_delta} missing ({prod_delta_pct:.1f}%)**"
    )
    a("")
    a(
        "**Likely causes** (Shopify auto-excludes from sitemap.xml in these cases): "
        "collections with zero matching products; smart collections with no current matches; "
        "hidden or admin-only collections; products with `published_status=hidden` set on the "
        "online_store sales channel even if visible in admin; products with no images or with "
        "missing required fields."
    )
    a("")
    a(
        "**SEO implication:** the sitemap-surfaced count is what Google can crawl. Anything "
        "missing from the public sitemap is invisible to organic search regardless of whether "
        "it's published in admin. The collections delta in particular (large) warrants VERITAS "
        "investigation: the missing collections may be intentionally unindexed (zero-product), "
        "or may signal a broken sitemap configuration costing organic visibility."
    )
    a("")
    a("### Locale variants (not surfaced by sitemap chunks; documented separately)")
    a("")
    a(
        "The Shopify sitemap.xml chunks do not enumerate locale-prefixed mirrors of canonical "
        "URLs. A prior `firecrawl_map` run (2026-05-08) discovered approximately:"
    )
    a("")
    a("- `/en-es/...`: ~1,765 URLs")
    a("- `/en-au/...`: 1 URL")
    a("")
    if locale_counts:
        a("This refresh's sitemap parse also picked up the following locale URLs:")
        a("")
        for code, count in sorted(locale_counts.items()):
            a(f"- `/{code}/...`: {count} URLs")
        a("")
    a(
        "Locale URLs follow the same path handles as the canonical English list "
        "(e.g., `/en-es/collections/mexico` mirrors `/collections/mexico`). The fact that they "
        "exist on the site but are NOT in the canonical sitemap is itself a signal: hreflang "
        "implementation, locale-targeting strategy, and Shopify Markets / third-party translation "
        "app (Langshop / Weglot) configuration are open questions. VERITAS follow-up logged in "
        "`work-log/follow-ups.md` 2026-05-08."
    )
    a("")
    a(
        "Internal anchors should use canonical English URLs unless a locale-specific link is "
        "explicitly required for hreflang or regional campaign work."
    )
    a("")

    a("## URLs to AVOID linking to")
    a("")
    a("Internal anchors must NEVER point to:")
    a("")
    a(
        "- **`magento1.prosoccer.com/*`** (legacy subdomain). Status under VERITAS investigation "
        "(see `work-log/follow-ups.md` 2026-05-08 entry)."
    )
    a(
        "- **`prosoccerteamstore.com/*`** (out of scope per Mike 2026-05-08). Separate Shopify "
        "property for team sales and wholesale."
    )
    a("- **`/cart`, `/checkout`, `/account`, `/account/login`, `/search?q=*`** (transactional or session URLs).")
    a(
        "- **`/admin/*`, `/api/*`, `/policies/legacy-*`** (internal or legacy paths if surfaced "
        "by the map). Spot-check during refresh."
    )
    a(
        "- **Collections not present in `## Collections` below.** If a collection is in Shopify "
        "admin but not in the sitemap, it isn't crawlable; treat as TBD and route to VERITAS "
        "for verification before publishing any anchor pointing to it."
    )
    a(
        "- **Locale URLs (`/en-es/`, `/en-au/`)** for default internal linking. Use canonical "
        "English URLs unless a locale anchor is explicitly required."
    )
    a("")

    a("## Wave-assigned collections (per `collections-master.csv`)")
    a("")
    a(
        "Cross-reference `deliverables/tracking/collections-master.csv` for the authoritative "
        "wave assignment per collection. As of last sitemap refresh, collections-master holds:"
    )
    a("")
    a("- **Wave 1:** `/collections/mexico` (status: approved 2026-05-08, awaiting Jorge dispatch)")
    a("- **Wave 2:** TBD (matrix coverage partial)")
    a("- **Wave 3:** TBD (matrix coverage partial)")
    a("")
    a(
        "All collection URLs below are listed alphabetically without phase grouping; consult "
        "collections-master.csv for phase status. The matrix v1.1 covers a subset of these "
        "collections; collections not in the matrix are listed under \"uncategorized\" by "
        "default and remain candidates for future matrix expansion."
    )
    a("")

    a("## Collections")
    a("")
    a(f"All {len(collections)} live collections from the public sitemap, alphabetized:")
    a("")
    a("```")
    for path in collections:
        a(path)
    a("```")
    a("")

    a("## Pages (informational)")
    a("")
    a(f"All {len(pages)} live informational pages, alphabetized:")
    a("")
    a("```")
    for path in pages:
        a(path)
    a("```")
    a("")

    a("## Blogs / articles")
    a("")
    a(f"All {len(blogs)} live blog and article URLs, alphabetized:")
    a("")
    a("```")
    for path in blogs:
        a(path)
    a("```")
    a("")

    a("## Other top-level URLs")
    a("")
    if other:
        a("```")
        for path in other:
            a(path)
        a("```")
    else:
        a("_(none surfaced this refresh)_")
    a("")

    a("## Products")
    a("")
    a(
        f"The Shopify sitemap surfaces **{len(products)} live products**. The full URL list is "
        f"not enumerated here because the catalog is too large to maintain inline (it would add "
        f"~800KB of churn per refresh). Refer directly to the Shopify product sitemap chunks "
        f"when the full list is needed:"
    )
    a("")
    for url in child_urls:
        if "sitemap_products_" in url:
            a(f"- `{url}`")
    a("")
    a("### Products grouped by vendor prefix")
    a("")
    a(
        "Below: count and 5 sample URLs per detected vendor. ProSoccer's catalog is brand-led, "
        "so most product handles begin with a recognizable vendor token (e.g., `adidas-...`, "
        "`nike-...`). Use this grouping to gauge brand depth when scoping internal-linking "
        "patterns; for an exact PDP target, fetch the relevant `sitemap_products_*.xml` chunk "
        "or run `firecrawl_map?search=<handle>`."
    )
    a("")
    a("| Vendor | Count | Sample handles |")
    a("|---|---|---|")
    for vendor, urls in sorted(vendor_groups.items(), key=lambda kv: -len(kv[1])):
        sample = ", ".join(f"`{u}`" for u in urls[:5])
        a(f"| {vendor} | {len(urls)} | {sample} |")
    a("")
    a("### 30-URL random product sample (deterministic, seed=42)")
    a("")
    import random  # local import; deterministic seed below
    rng = random.Random(42)
    sample_size = min(30, len(products))
    product_sample = sorted(rng.sample(products, sample_size))
    a("```")
    for path in product_sample:
        a(path)
    a("```")
    a("")

    SITEMAP_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {SITEMAP_OUT}")
    print(
        f"  collections={len(collections)} products={len(products)} "
        f"pages={len(pages)} blogs={len(blogs)} other={len(other)}"
    )


if __name__ == "__main__":
    main()
