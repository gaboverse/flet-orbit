import flet as ft

from ui import views


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

        # Content
        self.navbar_items = [
            NavBarItem(
                name = 'home',
                label = 'Home',
                icon = ft.Icons.HOME_ROUNDED,
                selected_icon = ft.Icons.HOME_ROUNDED,
                route = '/',
            ),
            NavBarItem(
                name = 'my_profile',
                label = 'My Profile',
                icon = ft.Icons.PERSON_OUTLINE_ROUNDED,
                selected_icon = ft.Icons.PERSON_ROUNDED,
                route = '/my',
            ),
        ]
    

        # Building
        for navbar_item in self.navbar_items:
            navbar_destination = ft.NavigationBarDestination(
                icon=navbar_item.icon,
                selected_icon=navbar_item.selected_icon,
                label=navbar_item.label,
            )
            self.destinations.append(navbar_destination)
    
    def get_event_route(self, e):
        route = self.navbar_items[int(e.data)].route
        return route
