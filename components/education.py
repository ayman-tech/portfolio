"""Education section with degree cards."""

from nicegui import ui
from data import EDUCATION
from components.shared import section_header


def create_education() -> None:
    with ui.element("section").props('id=education').classes(
        "w-full py-20 px-4 md:px-8 "
        "bg-slate-50/80 dark:bg-slate-800/30"
    ):
        with ui.column().classes("max-w-4xl mx-auto w-full"):
            section_header("Education")

            with ui.element("div").classes(
                "grid grid-cols-1 md:grid-cols-2 gap-6 w-full"
            ):
                for edu in EDUCATION:
                    with ui.card().classes(
                        "hover-lift !rounded-xl "
                        "!bg-white dark:!bg-slate-800/60 "
                        "!shadow-sm hover:!shadow-lg "
                        "border border-slate-200/50 dark:border-slate-700/50 "
                        "transition-all duration-300"
                    ):
                        # Icon + Degree
                        with ui.row().classes("items-center gap-3 mb-3"):
                            with ui.element("div").classes(
                                "w-12 h-12 rounded-xl "
                                "bg-indigo-500/10 dark:bg-indigo-500/20 "
                                "flex items-center justify-center shrink-0"
                            ):
                                ui.icon("school", size="sm").classes(
                                    "text-indigo-500"
                                )
                            with ui.column().classes("gap-0"):
                                ui.label(edu["degree"]).classes(
                                    "text-base font-bold text-slate-800 "
                                    "dark:text-slate-100 leading-snug"
                                )
                                ui.label(edu["school"]).classes(
                                    "text-sm text-indigo-600 "
                                    "dark:text-indigo-400 font-medium"
                                )

                        # Period
                        with ui.row().classes("items-center gap-1 mb-3"):
                            ui.icon("calendar_today", size="xs").classes(
                                "text-slate-400"
                            )
                            ui.label(edu["period"]).classes(
                                "text-sm text-slate-500 dark:text-slate-400"
                            )

                        # Courses
                        ui.label("Relevant Courses").classes(
                            "text-xs font-semibold uppercase tracking-wider "
                            "text-slate-400 dark:text-slate-500 mb-2"
                        )
                        with ui.row().classes("gap-2 flex-wrap"):
                            for course in edu["courses"]:
                                ui.label(course).classes(
                                    "px-2.5 py-1 rounded-full text-xs "
                                    "font-medium bg-indigo-50 text-indigo-700 "
                                    "dark:bg-indigo-900/30 dark:text-indigo-300"
                                )
