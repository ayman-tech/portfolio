"""Products showcase section."""

from nicegui import ui
from data import PROJECTS
from components.shared import section_header

# Gradient palette — one per card, cycles if more cards than colours
_GRADIENTS = [
    "from-indigo-600 via-purple-600 to-violet-700",
    "from-cyan-600 via-sky-600 to-blue-700",
    "from-emerald-600 via-teal-600 to-green-700",
    "from-orange-500 via-amber-500 to-yellow-600",
]


def _open(url: str) -> None:
    ui.run_javascript(f'window.open("{url}", "_blank")')


def create_projects() -> None:
    with ui.element("section").props('id=projects').classes(
        "w-full py-20 px-4 md:px-8 !bg-white dark:!bg-slate-900"
    ):
        with ui.column().classes("max-w-5xl mx-auto w-full"):
            section_header("Products")

            ui.label(
                "A growing suite of AI-powered tools — each built as a standalone product."
            ).classes(
                "text-slate-500 dark:text-slate-400 text-sm md:text-base "
                "text-center -mt-8 mb-12"
            )

            with ui.element("div").classes(
                "grid grid-cols-1 sm:grid-cols-2 gap-6 w-full"
            ):
                for i, project in enumerate(PROJECTS):
                    grad = _GRADIENTS[i % len(_GRADIENTS)]
                    product_url = project.get("product_link")
                    github_url = project.get("link")
                    status = project.get("status", "Coming Soon")
                    is_live = status == "Live"

                    with ui.card().classes(
                        "!rounded-2xl overflow-hidden !p-0 "
                        "!bg-slate-50 dark:!bg-slate-800/60 "
                        "border border-slate-200/50 dark:border-slate-700/50 "
                        "transition-all duration-300 hover-lift "
                        "hover:!shadow-2xl hover:!shadow-indigo-500/10 "
                        + ("cursor-pointer" if is_live and product_url else "")
                    ) as card:
                        if is_live and product_url:
                            card.on(
                                "click",
                                lambda url=product_url: _open(str(url)),
                            )

                        # ── Gradient banner ──────────────────────────────────
                        with ui.element("div").classes(
                            f"bg-gradient-to-br {grad} px-6 py-5 "
                            "flex items-start justify-between gap-3"
                        ):
                            # Icon + name
                            with ui.row().classes("items-center gap-3 min-w-0"):
                                with ui.element("div").classes(
                                    "w-12 h-12 rounded-xl "
                                    "bg-white/15 backdrop-blur-sm "
                                    "flex items-center justify-center shrink-0 "
                                    "border border-white/20"
                                ):
                                    ui.icon(project["icon"], size="sm").classes("text-white")
                                ui.label(project["name"]).classes(
                                    "text-lg font-bold text-white leading-snug"
                                )

                            # Top-right: status badge + GitHub icon
                            with ui.row().classes("items-center gap-2 shrink-0"):
                                if is_live:
                                    with ui.element("div").classes(
                                        "flex items-center gap-1.5 "
                                        "bg-green-400/20 border border-green-400/40 "
                                        "rounded-full px-2.5 py-1"
                                    ):
                                        ui.element("span").classes(
                                            "w-1.5 h-1.5 rounded-full bg-green-400 animate-pulse"
                                        )
                                        ui.label(status).classes(
                                            "text-xs font-semibold text-green-300"
                                        )
                                else:
                                    with ui.element("div").classes(
                                        "bg-white/10 border border-white/20 "
                                        "rounded-full px-2.5 py-1"
                                    ):
                                        ui.label(status).classes(
                                            "text-xs font-medium text-white/70"
                                        )

                                # GitHub icon button
                                if github_url:
                                    ui.button(icon="img:/static/github.svg").props(
                                        "flat round dense size=md"
                                    ).classes(
                                        "!w-10 !h-10 !min-w-0 !p-1 "
                                        "bg-white/10 hover:bg-white/25 "
                                        "border border-white/20 "
                                        "transition-all duration-200"
                                    ).on("click.stop", lambda url=github_url: _open(str(url)))

                        # ── Card body ─────────────────────────────────────────
                        with ui.column().classes("px-6 py-5 gap-4"):
                            # Description
                            ui.label(project["description"]).classes(
                                "text-sm text-slate-600 dark:text-slate-300 leading-relaxed"
                            )

                            # Tech stack badges
                            with ui.row().classes("gap-1.5 flex-wrap"):
                                for tech in project["tech"]:
                                    ui.label(tech).classes(
                                        "px-2 py-0.5 rounded-md text-xs font-medium "
                                        "bg-slate-200/70 text-slate-600 "
                                        "dark:bg-slate-700/60 dark:text-slate-300"
                                    )

                            # ── Footer row ────────────────────────────────────
                            ui.separator().classes(
                                "!border-slate-200 dark:!border-slate-700/50 w-full"
                            )
                            with ui.row().classes("items-center justify-between w-full"):
                                if is_live and product_url:
                                    with ui.row().classes("items-center gap-1.5"):
                                        ui.icon("rocket_launch", size="xs").classes(
                                            "text-indigo-500"
                                        )
                                        ui.label("Launch App").classes(
                                            "text-sm font-semibold text-indigo-500"
                                        )
                                elif github_url:
                                    with ui.row().classes(
                                        "items-center gap-1.5 cursor-pointer"
                                    ).on("click.stop", lambda url=github_url: _open(str(url))):
                                        ui.icon("code", size="xs").classes(
                                            "text-slate-500 dark:text-slate-400"
                                        )
                                        ui.label("View on GitHub").classes(
                                            "text-sm font-semibold text-slate-500 dark:text-slate-400"
                                        )

                                ui.icon("arrow_forward", size="xs").classes(
                                    "text-slate-400 dark:text-slate-500"
                                )
