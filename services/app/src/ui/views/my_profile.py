import flet as ft

from utils.decorators import view

@view("/my")
class MyProfileView(ft.Column):
    def __init__(self):
        super().__init__()

        # Content
        text = ft.Text(value="My Profile!")
        self.controls.append(text)
