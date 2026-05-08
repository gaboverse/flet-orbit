import flet as ft

import orbit


@orbit.view("/profile")
class ProfileView(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls.append(ft.Text("My Profile!"))
