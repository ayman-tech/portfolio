"""Navigation header with dark/light mode toggle."""

from nicegui import ui
from components.shared import scroll_to

NAV_ITEMS = [
    ("projects", "Products"),
    ("experience", "Experience"),
    ("education", "Education"),
    ("skills", "Skills"),
]


def create_header(dark_mode) -> None:
    with ui.header(elevated=False).classes(
        "!bg-white/80 dark:!bg-slate-900/80 backdrop-blur-lg "
        "border-b border-slate-200/50 dark:border-slate-700/50 "
        "items-center justify-between px-4 md:px-8"
    ):
        # -- Logo / Home --
        ui.label("AS").classes(
            "text-2xl font-extrabold gradient-text cursor-pointer select-none"
        ).on(
            "click",
            lambda: ui.run_javascript(
                'window.scrollTo({top:0,behavior:"smooth"})'
            ),
        )

        # -- Desktop navigation --
        with ui.element("div").classes("hidden md:flex items-center gap-1"):
            for sid, label in NAV_ITEMS:
                ui.button(label, on_click=lambda s=sid: scroll_to(s)).props(
                    "flat no-caps"
                ).classes(
                    "!text-slate-600 dark:!text-slate-300 "
                    "hover:!text-indigo-500 dark:hover:!text-indigo-400 "
                    "!font-medium"
                )

        # -- Right-side controls --
        with ui.row().classes("items-center gap-1"):
            # Mobile hamburger menu
            with ui.element("div").classes("md:hidden"):
                with ui.button(icon="menu").props("flat round").classes(
                    "!text-slate-600 dark:!text-slate-300"
                ):
                    with ui.menu().classes(
                        "dark:!bg-slate-800"
                    ):
                        for sid, label in NAV_ITEMS:
                            ui.menu_item(
                                label,
                                on_click=lambda s=sid: scroll_to(s),
                            ).classes("dark:!text-slate-200")

            # Dark / Light toggle
            theme_btn = ui.button(icon="light_mode").props(
                "flat round size=sm"
            ).classes("!text-slate-600 dark:!text-slate-300")

            def toggle_theme() -> None:
                if dark_mode.value:
                    dark_mode.disable()
                    theme_btn.props("icon=dark_mode")
                else:
                    dark_mode.enable()
                    theme_btn.props("icon=light_mode")

            theme_btn.on("click", toggle_theme)
