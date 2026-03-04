"""Reusable UI utilities for portfolio components."""

from nicegui import ui


def section_header(title: str) -> None:
    """Render a centered section header with gradient underline."""
    with ui.column().classes("items-center mb-12"):
        ui.label(title).classes(
            "text-3xl md:text-4xl font-extrabold gradient-text"
        )
        ui.element("div").classes(
            "w-16 h-1 bg-gradient-to-r from-indigo-500 to-purple-500 "
            "rounded-full mt-3"
        )


def scroll_to(section_id: str) -> None:
    """Smooth-scroll to a section by its DOM id."""
    ui.run_javascript(
        f'document.getElementById("{section_id}")'
        f'.scrollIntoView({{behavior:"smooth"}})'
    )
