"""Hero / intro section with profile image placeholder."""

from pathlib import Path
from nicegui import ui
from data import PROFILE

_IMG_DIR = Path(__file__).resolve().parent.parent / "static" / "images"


def _find_profile_image() -> str | None:
    for ext in ("jpg", "jpeg", "png", "webp"):
        if (_IMG_DIR / f"profile.{ext}").exists():
            return f"/static/images/profile.{ext}"
    return None


def create_hero() -> None:
    with ui.element("section").props('id=about').classes(
        "w-full min-h-[90vh] flex items-center justify-center "
        "bg-gradient-to-br from-slate-50 via-white to-indigo-50/60 "
        "dark:from-slate-900 dark:via-slate-800 dark:to-indigo-950/40 "
        "px-4 md:px-8 py-20"
    ):
        with ui.element("div").classes(
            "flex flex-col-reverse md:flex-row items-center "
            "gap-10 md:gap-16 max-w-5xl w-full"
        ):
            # -- Text content --
            with ui.column().classes(
                "gap-4 flex-1 items-center md:items-start "
                "text-center md:text-left"
            ):
                ui.label("Hi there, I\u2019m").classes(
                    "text-lg text-slate-500 dark:text-slate-400 font-medium"
                )
                ui.label(PROFILE["name"]).classes(
                    "text-5xl md:text-6xl font-extrabold gradient-text "
                    "leading-tight"
                )
                ui.label(PROFILE["title"]).classes(
                    "text-xl md:text-2xl text-slate-700 dark:text-slate-200 "
                    "font-semibold"
                )
                ui.label(PROFILE["tagline"]).classes(
                    "text-base text-slate-500 dark:text-slate-400 "
                    "max-w-lg leading-relaxed"
                )

                # Location chip
                with ui.row().classes("items-center gap-1 mt-1"):
                    ui.icon("location_on", size="xs").classes("text-indigo-500")
                    ui.label(PROFILE["location"]).classes(
                        "text-slate-600 dark:text-slate-400 text-sm"
                    )

                # CTA buttons
                with ui.row().classes("gap-3 mt-4 flex-wrap justify-center md:justify-start"):
                    ui.button(
                        "Get In Touch",
                        icon="mail",
                        on_click=lambda: ui.run_javascript(
                            f'window.location.href="mailto:{PROFILE["email"]}"'
                        ),
                    ).props("unelevated rounded no-caps").classes(
                        "!bg-indigo-500 hover:!bg-indigo-600 !text-white"
                    )
                    ui.button(
                        "LinkedIn",
                        icon="open_in_new",
                        on_click=lambda: ui.run_javascript(
                            f'window.open("{PROFILE["linkedin"]}","_blank")'
                        ),
                    ).props("outline rounded no-caps").classes(
                        "!text-indigo-500 !border-indigo-500"
                    )
                    ui.button(
                        "GitHub",
                        icon="code",
                        on_click=lambda: ui.run_javascript(
                            f'window.open("{PROFILE["github"]}","_blank")'
                        ),
                    ).props("outline rounded no-caps").classes(
                        "!text-indigo-500 !border-indigo-500"
                    )

            # -- Profile image placeholder --
            profile_src = _find_profile_image()
            with ui.element("div").classes(
                "w-48 h-48 md:w-64 md:h-64 rounded-full overflow-hidden "
                "bg-gradient-to-br from-indigo-500 via-purple-500 to-cyan-500 "
                "flex items-center justify-center shadow-2xl shrink-0 "
                "ring-4 ring-white dark:ring-slate-800"
            ):
                if profile_src:
                    ui.image(profile_src).classes(
                        "w-full h-full object-cover"
                    )
                else:
                    # Placeholder initials — drop a profile.jpg in static/images/ to replace
                    ui.label("AS").classes(
                        "text-6xl md:text-7xl font-extrabold text-white "
                        "select-none"
                    )
