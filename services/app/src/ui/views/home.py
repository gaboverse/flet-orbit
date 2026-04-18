import flet as ft

from utils.decorators import view

@view("/")
class HomeView(ft.Column):
    def __init__(self):
        super().__init__()

        # Content
        text = ft.Text(value="Welcome Home!")
        self.controls.append(text)
