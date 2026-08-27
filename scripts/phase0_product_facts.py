"""Phase 0 product-fact extraction from a Shopify product JSON payload.

WHY THIS EXISTS
---------------
ProSoccer no longer puts colorways in FOOTWEAR product titles. The colorway lives
in a Shopify product option named `Color` at position 1, rendered on the PDP as a
swatch row. Batch 16 compared two Furon Elite pages on title alone, found them
"byte-identical", and pulled a SKU from the batch as a merchandising defect. They
were two distinct colorways and the defect was ours.

Rule: `context/workforce-conventions.md`, "The live title governs" -> THE COLORWAY
EXCEPTION. The title governs where it SPEAKS; on colorway it is silent by store
convention, so the `Color` option is authoritative there.

APPAREL HAS NO `Color` OPTION. Jersey PDPs expose only a size option. For apparel
`colorway` comes back None and that is CORRECT, not a gap. Callers must not treat
a blank colorway on a jersey as a missing value; see `is_apparel`.

FETCH STEP (not performed here; this module is pure so it can be tested offline):
    GET https://www.prosoccer.com/products/<handle>.json
then pass the decoded object to `extract()`.
"""
from __future__ import annotations

import re

# Option names seen carrying the colorway. Position is not trusted: match on name.
_COLOR_OPTION_NAMES = {"color", "colour"}

# Size option names seen in the catalogue. Used to classify footwear vs apparel.
_FOOTWEAR_SIZE_HINTS = ("shoe size",)
_APPAREL_SIZE_HINTS = ("apparel size",)


class SkuMismatch(Exception):
    """The SKU we were handed is not the SKU the fetched page carries."""


def _options(product: dict) -> list[dict]:
    opts = product.get("options") or []
    # Shopify returns either [{"name":..,"values":[..]}] or a bare ["Color", "Size"]
    # depending on endpoint. Normalize the bare form to the dict form.
    if opts and isinstance(opts[0], str):
        return [{"name": o, "values": []} for o in opts]
    return opts


def extract_colorway(product: dict) -> str | None:
    """Return the colorway string from the `Color` option, or None if absent.

    None on apparel is expected and correct. Never fall back to the handle, the
    pack name, or the title: pack names routinely contain colour words (Coral
    Blaze, Neon Tide, Black Pack) and are not colorways.
    """
    for opt in _options(product):
        if (opt.get("name") or "").strip().lower() in _COLOR_OPTION_NAMES:
            values = [v for v in (opt.get("values") or []) if v and str(v).strip()]
            if not values:
                return None
            # A PDP is one colorway; more than one value means the product model
            # changed shape and the caller should look rather than guess.
            return " | ".join(str(v).strip() for v in values)
    return None


def size_option(product: dict) -> tuple[str | None, list[str]]:
    """Return (option name, values) for the size option, or (None, [])."""
    for opt in _options(product):
        name = (opt.get("name") or "").strip()
        if name.lower() in _COLOR_OPTION_NAMES:
            continue
        if "size" in name.lower():
            return name, [str(v) for v in (opt.get("values") or [])]
    return None, []


def is_apparel(product: dict) -> bool:
    """True when the size option is an apparel ladder, so a missing Color option
    is absent BY DESIGN rather than a scrape gap."""
    name, _ = size_option(product)
    if not name:
        return False
    low = name.lower()
    if any(h in low for h in _APPAREL_SIZE_HINTS):
        return True
    if any(h in low for h in _FOOTWEAR_SIZE_HINTS):
        return False
    return False


def base_skus(product: dict) -> list[str]:
    """Distinct base SKUs across variants.

    Variant SKUs are `<BASE-SKU>-<size>`; the size segment is stripped by removing
    the trailing size token after the LAST hyphen that precedes a size-looking
    value. Sizes contain digits and may contain '/', 'K', '.', and spaces, so the
    split is done against the product's own size values rather than by guesswork.
    """
    _, sizes = size_option(product)
    seen, out = set(), []
    for v in product.get("variants") or []:
        sku = (v.get("sku") or "").strip()
        if not sku:
            continue
        base = sku
        for s in sizes:
            suffix = "-%s" % s
            if sku.endswith(suffix):
                base = sku[: -len(suffix)]
                break
        else:
            # Fall back to the variant's own option value if sizes were unavailable.
            opt = (v.get("option2") or v.get("option1") or "").strip()
            if opt and sku.endswith("-%s" % opt):
                base = sku[: -len(opt) - 1]
        if base not in seen:
            seen.add(base)
            out.append(base)
    return out


def verify_sku(expected_sku: str, product: dict) -> str:
    """Confirm the SKU we were handed matches the page we fetched.

    Returns the matched base SKU. Raises SkuMismatch otherwise. This is the check
    that would have caught the Batch 16 18282 handle-versus-SKU contradiction
    automatically instead of by inspection.
    """
    expected = (expected_sku or "").strip()
    if not expected:
        raise SkuMismatch("no expected SKU supplied")
    found = base_skus(product)
    if not found:
        raise SkuMismatch(
            "page %r exposes no variant SKUs, cannot verify %r"
            % (product.get("handle"), expected)
        )
    for b in found:
        if b.upper() == expected.upper():
            return b
    raise SkuMismatch(
        "expected SKU %r not found on page %r; page carries %s"
        % (expected, product.get("handle"), ", ".join(repr(f) for f in found))
    )


def extract(product: dict, expected_sku: str | None = None) -> dict:
    """Phase 0 product facts. Raises SkuMismatch when expected_sku disagrees."""
    name, values = size_option(product)
    apparel = is_apparel(product)
    colorway = extract_colorway(product)
    facts = {
        "handle": product.get("handle"),
        "colorway": colorway,
        "colorway_absent_by_design": colorway is None and apparel,
        "is_apparel": apparel,
        "size_option_name": name,
        "size_values": values,
        "base_skus": base_skus(product),
    }
    if expected_sku is not None:
        facts["verified_sku"] = verify_sku(expected_sku, product)
    return facts


def input_line(facts: dict) -> str:
    """The line Phase 0 writes into the per-SKU input file.

    Apparel gets an explicit statement rather than a blank, so a future reader
    does not read absence as an omission.
    """
    if facts["colorway"] is not None:
        return "- Colorway (Color option): %s" % facts["colorway"]
    if facts["colorway_absent_by_design"]:
        return ("- Colorway (Color option): NOT APPLICABLE. This is apparel and "
                "apparel PDPs carry no Color option. Absent by design, not a gap. "
                "Take colorway from the scraped description prose, and where the "
                "prose is silent state no colorway at all.")
    return ("- Colorway (Color option): ABSENT and this is NOT apparel. Do not "
            "invent one. Escalate: a footwear PDP with no Color option is unexpected.")
