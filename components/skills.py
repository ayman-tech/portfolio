"""Skills section with categorized badge groups."""

from nicegui import ui
from data import SKILLS
from components.shared import section_header


def create_skills() -> None:
    with ui.element("section").props('id=skills').classes(
        "w-full py-20 px-4 md:px-8 "
        "bg-slate-50/80 dark:bg-slate-800/30"
    ):
        with ui.column().classes("max-w-5xl mx-auto w-full"):
            section_header("Skills")

            with ui.element("div").classes(
                "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-full"
            ):
                for category, info in SKILLS.items():
                    with ui.card().classes(
                        "hover-lift !rounded-xl "
                        "!bg-white dark:!bg-slate-800/60 "
                        "!shadow-sm hover:!shadow-lg "
                        "border border-slate-200/50 dark:border-slate-700/50 "
                        "transition-all duration-300"
                    ):
                        with ui.row().classes("items-center gap-2 mb-4"):
                            ui.icon(info["icon"], size="sm").classes(
                                "text-indigo-500"
                            )
                            ui.label(category).classes(
                                "text-base font-bold text-slate-800 "
                                "dark:text-slate-100"
                            )

                        with ui.row().classes("gap-2 flex-wrap"):
                            for skill in info["items"]:
                                ui.label(skill).classes(
                                    "px-3 py-1 rounded-full text-xs "
                                    "font-medium bg-indigo-50 text-indigo-700 "
                                    "dark:bg-indigo-900/30 dark:text-indigo-300 "
                                    "transition-colors"
                                )
