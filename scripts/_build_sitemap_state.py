"""One-shot generator for deliverables/tracking/sitemap-state.md.

Reads the firecrawl_map JSON output, categorizes URLs, writes the markdown file.
Intentionally local-only; not invoked from any agent runtime path.
"""
from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

REPO = Path(__file__).resolve().parent.parent
FIRECRAWL_OUT = Path(
    r"C:\Users\Ashot\.claude\projects\C--Dev-Projects-marketing-prosoccer-seo\0e81e760-b53d-4f3a-a43e-8a9e4f193bda\tool-results\mcp-firecrawl-mcp-firecrawl_map-1778278322714.txt"
)
SITEMAP_OUT = REPO / "deliverables" / "tracking" / "sitemap-state.md"

DATE = "2026-05-08"


def main() -> None:
    raw = json.loads(FIRECRAWL_OUT.read_text(encoding="utf-8"))
    links = raw.get("links", [])

    LOCALE_PREFIXES = ("/en-es/", "/en-au/", "/en-ca/", "/en-gb/")
    locale_counts: dict[str, int] = defaultdict(int)
    paths: set[str] = set()
    for entry in links:
        url = entry.get("url", "")
        parsed = urlparse(url)
        if not parsed.path:
            continue
        if parsed.netloc not in {"www.prosoccer.com", "prosoccer.com"}:
            continue
        path = parsed.path.rstrip("/") or "/"
        # Strip locale prefix and count it
        for prefix in LOCALE_PREFIXES:
            if path.startswith(prefix):
                locale_counts[prefix.strip("/")] += 1
                path = "/" + path[len(prefix):]
                break
        paths.add(path)

    buckets: dict[str, list[str]] = defaultdict(list)
    others: list[str] = []
    for path in sorted(paths):
        if path.startswith("/collections/"):
            buckets["collections"].append(path)
        elif path.startswith("/products/"):
            buckets["products"].append(path)
        elif path.startswith("/blogs/"):
            buckets["blogs"].append(path)
        elif path.startswith("/pages/"):
            buckets["pages"].append(path)
        else:
            others.append(path)

    rng = random.Random(42)
    product_sample = sorted(rng.sample(buckets["products"], min(20, len(buckets["products"]))))

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
    a(f"**Last refreshed:** {DATE} via `firecrawl_map` against `https://www.prosoccer.com`.")
    a("")
    a("## Refresh protocol")
    a("")
    a(
        "- **Cadence:** every Monday morning. ORIN runs `firecrawl_map` against "
        "`https://www.prosoccer.com`, regenerates this file via `scripts/_build_sitemap_state.py`, "
        "and logs the refresh in `work-log/follow-ups.md` (or in `deliverables/tracking/technical-seo-log.md` "
        "once that surface absorbs site-state events)."
    )
    a(
        "- **Ad-hoc refresh** when a major URL change ships (collection rename, redirect campaign, "
        "new product line launch). Note the trigger in `work-log/` rather than waiting for Monday."
    )
    a(
        "- **Cost:** firecrawl_map of `prosoccer.com` returns roughly 9,000 link entries and counts "
        "as one map call against the Firecrawl free-tier 800-credit ceiling. Single-digit credits per refresh."
    )
    a("")
    a("## Counts (per refresh, canonical English paths only)")
    a("")
    a(f"- Collections: {len(buckets['collections'])}")
    a(f"- Products: {len(buckets['products'])}")
    a(f"- Blogs/articles: {len(buckets['blogs'])}")
    a(f"- Pages (informational): {len(buckets['pages'])}")
    a(f"- Other top-level URLs: {len(others)}")
    a("")
    a("### Locale variants (mirror canonical paths under locale prefixes)")
    a("")
    if locale_counts:
        for code, count in sorted(locale_counts.items()):
            a(f"- `/{code}/...`: {count} URLs")
    else:
        a("- (none detected this refresh)")
    a("")
    a(
        "Locale URLs follow the same path handles as the canonical English list "
        "(e.g., `/en-es/collections/mexico` mirrors `/collections/mexico`). "
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
        "- **`prosoccerteamstore.com/*`** (out of scope per Mike 2026-05-08). Separate Shopify property "
        "for team sales and wholesale."
    )
    a("- **`/cart`, `/checkout`, `/account`, `/account/login`, `/search?q=*`** (transactional or session URLs).")
    a(
        "- **`/admin/*`, `/api/*`, `/policies/legacy-*`** (internal or legacy paths if surfaced by the map). "
        "Spot-check during refresh."
    )
    a(
        "- **Any URL not present in the lists below.** If SCRIBE proposes an anchor and the destination "
        "isn't in this file, treat as TBD and route to VERITAS for verification before publish."
    )
    a("")

    a("## Wave-assigned collections (per `collections-master.csv`)")
    a("")
    a(
        "Cross-reference `deliverables/tracking/collections-master.csv` for the authoritative wave "
        "assignment per collection. As of last sitemap refresh, collections-master holds:"
    )
    a("")
    a("- **Wave 1:** `/collections/mexico` (status: approved 2026-05-08, awaiting Jorge dispatch)")
    a("- **Wave 2:** TBD")
    a("- **Wave 3:** TBD")
    a("")
    a("All collection URLs below are listed alphabetically without phase grouping; consult collections-master.csv for phase status.")
    a("")

    a("## Collections")
    a("")
    a("```")
    for path in buckets["collections"]:
        a(path)
    a("```")
    a("")

    a("## Blogs / articles")
    a("")
    a("```")
    for path in buckets["blogs"]:
        a(path)
    a("```")
    a("")

    a("## Pages (informational)")
    a("")
    a("```")
    for path in buckets["pages"]:
        a(path)
    a("```")
    a("")

    a("## Other top-level URLs")
    a("")
    a("```")
    for path in others:
        a(path)
    a("```")
    a("")

    a("## Products (sample of 20; full list of " f"{len(buckets['products'])} products is not inlined)")
    a("")
    a(
        "Product URLs are not enumerated in this file because the catalog is too large to maintain "
        "manually and changes daily. SCRIBE proposes product anchors only when KIRA flags a specific "
        "PDP as a target; verify via `firecrawl_map?search=<product handle>` or a direct fetch before publish."
    )
    a("")
    a("```")
    for path in product_sample:
        a(path)
    a("```")
    a("")

    SITEMAP_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {SITEMAP_OUT}")
    print(
        f"  collections={len(buckets['collections'])} products={len(buckets['products'])} "
        f"blogs={len(buckets['blogs'])} pages={len(buckets['pages'])} other={len(others)}"
    )


if __name__ == "__main__":
    main()
