import flet as ft


class AppBarComponent(ft.AppBar):
    def __init__(self):
        super().__init__()

        self.title = AppBarTitle()
        self.center_title = True
        self.bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST

        self.actions = [ft.IconButton(ft.Icons.NOTIFICATIONS_NONE_ROUNDED)]

class AppBarTitle(ft.Text):
    def __init__(self):
        super().__init__()

        self.spans = [
            ft.TextSpan(
                text = 'flet',
                style = ft.TextStyle(
                    weight = 'BOLD',
                ),
            ),
            ft.TextSpan(
                text = 'flow',
                style = ft.TextStyle(
                    weight = 'NORMAL',
                ),
            ),
        ]
