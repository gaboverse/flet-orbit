import flet as ft

class MyAppTheme(ft.Theme):
    # https://flet.dev/docs/reference/types/theme/
    def __init__(self):
        super().__init__()

        self.color_scheme = MyAppColorScheme()


class MyAppColorScheme(ft.ColorScheme):
    # https://flet.dev/docs/reference/types/colorscheme/
    def __init__(self):
        super().__init__()

        self.primary = ft.Colors.BLUE_400
        self.background = ft.Colors.GREY_200
