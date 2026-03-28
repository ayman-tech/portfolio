"""Portfolio website – entry point."""

import os
from pathlib import Path

from nicegui import app, ui

from components import (
    create_education,
    create_experience,
    create_footer,
    create_header,
    create_hero,
    create_projects,
    create_skills,
)

STATIC_DIR = Path(__file__).resolve().parent / "static"

# ---------------------------------------------------------------------------
# Custom CSS injected into every page
# ---------------------------------------------------------------------------
_CUSTOM_CSS = """
<style>
    html { scroll-behavior: smooth; }

    .hover-lift {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .hover-lift:hover {
        transform: translateY(-6px);
    }

    .gradient-text {
        background: linear-gradient(135deg, #6366f1, #8b5cf6, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* offset anchors for the fixed header */
    section { scroll-margin-top: 80px; }
</style>
"""


# ---------------------------------------------------------------------------
# Page
# ---------------------------------------------------------------------------
@ui.page("/")
def index():
    ui.colors(
        primary="#6366f1",
        secondary="#8b5cf6",
        accent="#06b6d4",
        dark_page="#0f172a",
    )

    ui.add_head_html('<meta name="darkreader-lock">')
    ui.add_head_html(
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">'
    )
    ui.add_head_html(_CUSTOM_CSS)
    ui.query("body").style("font-family: 'Inter', sans-serif;")

    dark = ui.dark_mode(True)

    create_header(dark)

    with ui.column().classes("w-full items-center !gap-0"):
        create_hero()
        create_projects()
        create_experience()
        create_education()
        create_skills()
        create_footer()


# ---------------------------------------------------------------------------
# Startup
# ---------------------------------------------------------------------------
def main():
    (STATIC_DIR / "images").mkdir(parents=True, exist_ok=True)
    app.add_static_files("/static", str(STATIC_DIR))
    ui.run(
        title="Ayman Sayed",
        favicon="⚡",
        storage_secret="portfolio-secret-key",
        host="0.0.0.0", # for Docker
        port=int(os.environ.get("PORT", 8080)), # for docker
    )


if __name__ in {"__main__", "__mp_main__"}:
    main()
