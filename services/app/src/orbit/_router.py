import flet as ft

from orbit._view import get_view
from orbit._exceptions import ViewNotFoundError


class Router:
    """
    Declarative router that listens for route changes (``page.on_route_change``)
    and automatically renders the matching registered view.
    """

    def __init__(self, page: ft.Page, content_container: ft.Control = None):
        self.page = page
        self.content_container = content_container or page
        page.on_route_change = self._handle_route_change

    def navigate(self, route: str):
        """Change the page route, triggering ``on_route_change``."""
        self.page.go(route)

    def _handle_route_change(self, e: ft.RouteChangeEvent):
        """Internal callback that resolves and renders the view."""
        route = self.page.route or "/"
        try:
            ViewClass = get_view(route)
        except ViewNotFoundError:
            self._render_not_found(route)
            return
        view_instance = ViewClass()
        self._render(view_instance)

    def _render(self, view_instance: ft.Control):
        """Place the view instance in the appropriate container."""
        if isinstance(self.content_container, ft.Page):
            if self.page.controls:
                self.page.controls.pop()
            self.page.controls.append(view_instance)
        else:
            self.content_container.content = view_instance
        self.page.update()

    def _render_not_found(self, route: str):
        """Render a default view when the route is not registered."""
        not_found = ft.Column(
            [
                ft.Text("404", size=48, weight=ft.FontWeight.BOLD),
                ft.Text(f"Route '{route}' not found.", size=16),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
        self._render(not_found)
