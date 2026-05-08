import flet as ft


class NavBarItem:
    def __init__(self, name, label, icon, selected_icon, route):
        self.name = name
        self.label = label
        self.icon = icon
        self.selected_icon = selected_icon
        self.route = route


class NavBarComponent(ft.NavigationBar):
    def __init__(self):
        super().__init__()

        self.navbar_items = [
            NavBarItem(
                name="home",
                label="Home",
                icon=ft.Icons.HOME_ROUNDED,
                selected_icon=ft.Icons.HOME_ROUNDED,
                route="/",
            ),
            NavBarItem(
                name="profile",
                label="My Profile",
                icon=ft.Icons.PERSON_OUTLINE_ROUNDED,
                selected_icon=ft.Icons.PERSON_ROUNDED,
                route="/profile",
            ),
        ]

        for item in self.navbar_items:
            destination = ft.NavigationBarDestination(
                icon=item.icon,
                selected_icon=item.selected_icon,
                label=item.label,
            )
            self.destinations.append(destination)

    def get_event_route(self, e):
        return self.navbar_items[int(e.data)].route
