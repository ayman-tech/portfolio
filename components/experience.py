"""Work experience section with timeline-style cards."""

from nicegui import ui
from data import EXPERIENCE
from components.shared import section_header


def create_experience() -> None:
    with ui.element("section").props('id=experience').classes(
        "w-full py-20 px-4 md:px-8 !bg-white dark:!bg-slate-900"
    ):
        with ui.column().classes("max-w-4xl mx-auto w-full"):
            section_header("Experience")

            for exp in EXPERIENCE:
                with ui.card().classes(
                    "w-full hover-lift !rounded-xl "
                    "!bg-slate-50 dark:!bg-slate-800/50 "
                    "!shadow-sm hover:!shadow-lg border-l-4 !border-indigo-500 "
                    "border border-slate-200/50 dark:border-slate-700/50 "
                    "transition-all duration-300 mb-5"
                ):
                    # Role & Company
                    with ui.row().classes(
                        "w-full justify-between items-start flex-wrap gap-2"
                    ):
                        with ui.column().classes("gap-1"):
                            ui.label(exp["role"]).classes(
                                "text-lg font-bold text-slate-800 "
                                "dark:text-slate-100"
                            )
                            with ui.row().classes("items-center gap-2"):
                                ui.icon("business", size="xs").classes(
                                    "text-indigo-500"
                                )
                                ui.label(exp["company"]).classes(
                                    "text-indigo-600 dark:text-indigo-400 "
                                    "font-semibold text-sm"
                                )

                        # Period & Location
                        with ui.column().classes("items-end gap-1"):
                            with ui.row().classes("items-center gap-1"):
                                ui.icon("calendar_today", size="xs").classes(
                                    "text-slate-400"
                                )
                                ui.label(exp["period"]).classes(
                                    "text-sm text-slate-500 dark:text-slate-400"
                                )
                            with ui.row().classes("items-center gap-1"):
                                ui.icon("location_on", size="xs").classes(
                                    "text-slate-400"
                                )
                                ui.label(exp["location"]).classes(
                                    "text-sm text-slate-500 dark:text-slate-400"
                                )

                    ui.separator().classes("my-3 dark:!bg-slate-700")

                    # Bullet points
                    with ui.column().classes("gap-2"):
                        for bullet in exp["bullets"]:
                            with ui.row().classes("gap-2 items-start !flex-nowrap"):
                                ui.label("▸").classes(
                                    "text-indigo-500 mt-px shrink-0 text-sm"
                                )
                                ui.label(bullet).classes(
                                    "text-slate-600 dark:text-slate-300 "
                                    "text-sm leading-relaxed"
                                )
