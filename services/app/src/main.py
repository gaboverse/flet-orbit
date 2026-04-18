import flet as ft

from ui.components.appbar import AppBarComponent
from ui.components.navbar import NavBarComponent

import ui.views

from utils.loaders import get_view
from utils.helpers import navigate

def main(page: ft.Page):

    # +------------+
    # | App Layout |
    # +------------+

    page.title = "Example"
    page.appbar = AppBarComponent()
    page.navigation_bar = NavBarComponent()


    # +--------------+
    # | Initial view |
    # +--------------+

    ViewClass = get_view('/')
    view_instance = ViewClass()  # Instantiate the view
    page.controls.append(view_instance)
    page.update()

    # +-----------------+
    # | Events Handlers |
    # +-----------------+

    # Navigation: NavBar
    def navbar_navigate(e):
        route = page.navigation_bar.get_event_route(e)
        navigate(page, route)


    # +-----------------+
    # | Events Triggers |
    # +-----------------+

    # Navigation: Navbar
    page.navigation_bar.on_change = navbar_navigate


ft.app(main, assets_dir="assets")
