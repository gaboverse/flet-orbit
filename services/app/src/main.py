import flet as ft

from ui.components.appbar import AppBarComponent
from ui.components.navbar import NavBarComponent
import orbit


def main(page: ft.Page):
    # App layout
    page.title = "Example"
    page.appbar = AppBarComponent()
    page.navigation_bar = NavBarComponent()

    # View discovery
    orbit.load_views("ui.views")

    # Router
    router = orbit.Router(page)

    # Event handlers
    def navbar_navigate(e):
        route = page.navigation_bar.get_event_route(e)
        router.navigate(route)

    # Event triggers
    page.navigation_bar.on_change = navbar_navigate

    # Initial route
    router.navigate(page.route or "/")


ft.run(main, assets_dir="assets")
