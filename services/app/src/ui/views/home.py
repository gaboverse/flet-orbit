import flet as ft

import orbit


@orbit.view("/")
class HomeView(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls.append(ft.Text("Welcome Home!"))
