"""Footer with social links and copyright."""

from nicegui import ui
from data import PROFILE


def create_footer() -> None:
    with ui.element("footer").classes(
        "w-full bg-slate-900 dark:bg-slate-950"
    ):
        with ui.column().classes("w-full items-center py-8 gap-4"):
            # Social links
            with ui.row().classes("gap-3"):
                _social_btn(
                    "mail",
                    f'mailto:{PROFILE["email"]}',
                )
                _social_btn(
                    "language",
                    PROFILE["website"],
                )
                _social_btn(
                    "code",
                    PROFILE["github"],
                )

            ui.separator().classes("!bg-slate-700/50 w-32")

            ui.label(
                f'\u00a9 2025 {PROFILE["name"]}. All rights reserved.'
            ).classes("text-sm text-slate-500")


def _social_btn(icon: str, url: str) -> None:
    ui.button(
        icon=icon,
        on_click=lambda u=url: ui.run_javascript(
            f'window.open("{u}","_blank")'
        ),
    ).props("flat round").classes(
        "!text-slate-400 hover:!text-indigo-400 transition-colors"
    )
