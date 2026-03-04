"""Projects showcase section."""

from nicegui import ui
from data import PROJECTS
from components.shared import section_header


def create_projects() -> None:
    with ui.element("section").props('id=projects').classes(
        "w-full py-20 px-4 md:px-8 !bg-white dark:!bg-slate-900"
    ):
        with ui.column().classes("max-w-5xl mx-auto w-full"):
            section_header("Projects")

            with ui.element("div").classes(
                "grid grid-cols-1 sm:grid-cols-2 gap-6 w-full"
            ):
                for project in PROJECTS:
                    with ui.card().classes(
                        "hover-lift !rounded-xl "
                        "!bg-slate-50 dark:!bg-slate-800/50 "
                        "!shadow-sm hover:!shadow-lg "
                        "border border-slate-200/50 dark:border-slate-700/50 "
                        "transition-all duration-300"
                    ):
                        # Icon + title
                        with ui.row().classes("items-center gap-3 mb-3"):
                            with ui.element("div").classes(
                                "w-10 h-10 rounded-lg "
                                "bg-indigo-500/10 dark:bg-indigo-500/20 "
                                "flex items-center justify-center shrink-0"
                            ):
                                ui.icon(project["icon"], size="sm").classes(
                                    "text-indigo-500"
                                )
                            ui.label(project["name"]).classes(
                                "text-lg font-bold text-slate-800 "
                                "dark:text-slate-100"
                            )

                        # Description
                        ui.label(project["description"]).classes(
                            "text-sm text-slate-600 dark:text-slate-300 "
                            "leading-relaxed mb-3"
                        )

                        # Tech badges
                        with ui.row().classes("gap-1.5 flex-wrap"):
                            for tech in project["tech"]:
                                ui.label(tech).classes(
                                    "px-2 py-0.5 rounded-md text-xs "
                                    "font-medium bg-indigo-50 text-indigo-700 "
                                    "dark:bg-indigo-900/30 dark:text-indigo-300"
                                )

                        # GitHub link
                        if project.get("link"):
                            with ui.row().classes("mt-3"):
                                ui.button(
                                    "View on GitHub",
                                    icon="open_in_new",
                                    on_click=lambda url=project["link"]: (
                                        ui.run_javascript(
                                            f'window.open("{url}","_blank")'
                                        )
                                    ),
                                ).props("flat no-caps size=sm").classes(
                                    "!text-indigo-500 hover:!text-indigo-600"
                                )
