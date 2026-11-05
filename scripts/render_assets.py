"""Render the static pixel-playbill SVGs into assets/."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from playbill import (  # noqa: E402
    DARK,
    LIGHT,
    build_divider,
    build_font_proof,
    build_footer,
    build_hero,
    build_link,
    build_pipeline,
    build_poster,
    build_stats,
    save_svg,
)

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

POSTERS = [
    (
        "macro.svg",
        "MACRO BY MARK",
        "ECONOMICS + U.S. MACRO RESEARCH",
        "#FFE14A",
        "lemon",
        "Macro by Mark, economics learning and U.S. macro research",
    ),
    (
        "riff.svg",
        "GETRIFF",
        "IOS WORKOUT APP IN TESTFLIGHT",
        "#FF8EC4",
        "riff",
        "getriff, an iOS workout app in TestFlight",
    ),
    (
        "ipedsdb.svg",
        "IPEDSDB PANEL",
        "147,782 x 2,676  /  2004-2024",
        "#5EECC0",
        "grid",
        "IPEDSDB_Panel. 2004-2024 consolidated file: 147,782 rows by 2,676 columns. Labeled release full-panel-labels-v1: 141,711 by 2,721. A 39-check acceptance audit.",
    ),
    (
        "fsa.svg",
        "FSA VOLUME PANEL",
        "25+ YEARS OF TITLE IV VOLUME",
        "#FFC44D",
        "coins",
        "FSAVolumeReports_Panel, 25-plus years of Title IV volume reports",
    ),
    (
        "ipeds-fsa.svg",
        "IPEDS-FSA PANEL",
        "AID REPORTS LINKED TO IPEDS",
        "#C4A6FF",
        "link",
        "IPEDS-FSA_Panel, Federal Student Aid reports linked to IPEDS",
    ),
    (
        "paneling.svg",
        "IPEDS PANELING",
        "DUCKDB PIPELINE FOR NCES IPEDS",
        "#9FD4FF",
        "stack",
        "IPEDS_Paneling, a DuckDB pipeline for NCES IPEDS",
    ),
    (
        "coa.svg",
        "COA FINAID SUBS",
        "COST-OF-ATTENDANCE REPLICATION",
        "#FFB070",
        "scroll",
        "COA_FINAID_SUBS, replication code for cost-of-attendance research",
    ),
    (
        "site.svg",
        "MARKJAYSON.COM",
        "PERSONAL SITE  /  ASTRO",
        "#FFE14A",
        "house",
        "markjaysonwebsite-v2, personal site built with Astro",
    ),
    (
        "creative.svg",
        "CREATIVE WORKS",
        "PORTFOLIO  /  CLOUDFLARE PAGES",
        "#FF8EC4",
        "mask",
        "creative-markjayson, creative portfolio on Cloudflare Pages",
    ),
]

LINKS = [
    ("website.svg", "WEBSITE", "#FFE14A"),
    ("linkedin.svg", "LINKEDIN", "#9FD4FF"),
    ("email.svg", "EMAIL", "#FF8EC4"),
    ("letterboxd.svg", "LETTERBOXD", "#5EECC0"),
]


def main() -> None:
    save_svg(
        ASSETS / "hero-light.svg",
        build_hero(LIGHT),
        "The Earl of Lemongrab presents Mark Jayson Farol, quantitative economist, in a pixel Land of Ooo.",
        "Pixel playbill header. Mark Jayson Farol, quantitative economist, Las Vegas.",
    )
    save_svg(
        ASSETS / "hero-dark.svg",
        build_hero(DARK),
        "The Earl of Lemongrab presents Mark Jayson Farol, quantitative economist, in a pixel Land of Ooo.",
        "Pixel playbill header for dark mode. Mark Jayson Farol, quantitative economist, Las Vegas.",
    )
    save_svg(
        ASSETS / "stats-light.svg",
        build_stats(LIGHT),
        "By the numbers: 2004-2024 IPEDS panel 147,782 by 2,676; labeled release 141,711 by 2,721; a 39-check acceptance audit; 25-plus years of Title IV volume; 200-plus students a term; 10 researchers mentored.",
        "Six pixel tickets. The 2004-2024 consolidated IPEDS file is 147,782 by 2,676. The labeled release is 141,711 by 2,721. The acceptance audit runs 39 checks.",
    )
    save_svg(
        ASSETS / "stats-dark.svg",
        build_stats(DARK),
        "By the numbers: 2004-2024 IPEDS panel 147,782 by 2,676; labeled release 141,711 by 2,721; a 39-check acceptance audit; 25-plus years of Title IV volume; 200-plus students a term; 10 researchers mentored.",
        "Six pixel tickets for dark mode. The 2004-2024 consolidated IPEDS file is 147,782 by 2,676. The labeled release is 141,711 by 2,721. The acceptance audit runs 39 checks.",
    )
    save_svg(
        ASSETS / "divider.svg",
        build_divider(),
        "",
        "Pixel lemon divider.",
    )
    save_svg(
        ASSETS / "pipeline-light.svg",
        build_pipeline(LIGHT),
        "From public sources through reproducible pipelines to panels, Macro by Mark, and working papers.",
        "Pixel diagram: NCES IPEDS, student aid, and macro sources flow through DuckDB and QA into panels and products.",
    )
    save_svg(
        ASSETS / "pipeline-dark.svg",
        build_pipeline(DARK),
        "From public sources through reproducible pipelines to panels, Macro by Mark, and working papers.",
        "Pixel diagram for dark mode: sources, pipelines, and research output.",
    )
    save_svg(
        ASSETS / "footer-light.svg",
        build_footer(LIGHT),
        "Mark Jayson Farol, Las Vegas, with the two Lemongrab twins on a candy hill.",
        "Closing pixel curtain.",
    )
    save_svg(
        ASSETS / "footer-dark.svg",
        build_footer(DARK),
        "Mark Jayson Farol, Las Vegas, with the two Lemongrab twins on a candy hill.",
        "Closing pixel curtain for dark mode.",
    )
    for filename, title, subtitle, accent, icon, desc in POSTERS:
        save_svg(
            ASSETS / "posters" / filename,
            build_poster(title, subtitle, accent, icon),
            title,
            desc,
        )
    for filename, label, accent in LINKS:
        save_svg(
            ASSETS / "links" / filename,
            build_link(label, accent),
            label,
            label,
        )
    if "--proof" in sys.argv:
        save_svg(Path("/tmp/font-proof.svg"), build_font_proof(), "Font proof", "Glyph proof sheet.")


if __name__ == "__main__":
    main()
