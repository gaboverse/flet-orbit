"""View system: registration, discovery, resolution and navigation."""

import importlib
import pkgutil
import sys

import flet as ft

from orbit._exceptions import ViewNotFoundError

# ---------------------------------------------------------------------------
# Internal registry (private)
# ---------------------------------------------------------------------------
_VIEW_REGISTRY: dict[str, tuple[str, str]] = {}


def view(route: str):
    """Decorator that registers a class as a view for a given route."""

    def decorator(cls):
        _VIEW_REGISTRY[route] = (cls.__module__, cls.__name__)
        return cls

    return decorator


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def load_views(package_name: str):
    """Recursively imports all modules in a package to trigger @view."""
    package = importlib.import_module(package_name)
    for _, module_name, is_pkg in pkgutil.walk_packages(
        package.__path__, package.__name__ + "."
    ):
        importlib.import_module(module_name)


# ---------------------------------------------------------------------------
# Resolution
# ---------------------------------------------------------------------------
def get_view(route: str):
    """Return the view class registered for a route."""
    if route not in _VIEW_REGISTRY:
        raise ViewNotFoundError(f"Route '{route}' not found.")
    module_name, class_name = _VIEW_REGISTRY[route]
    module = sys.modules.get(module_name)
    if module is None:
        raise ImportError(f"Module '{module_name}' not loaded.")
    return getattr(module, class_name)


# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------
def navigate(page: ft.Page, route: str):
    """
    Navigate to *route* by replacing the last control in ``page.controls``.
    If ``page.controls`` is empty, the view is simply appended.
    """
    ViewClass = get_view(route)
    view_instance = ViewClass()
    if page.controls:
        page.controls.pop()
    page.controls.append(view_instance)
    page.route = route
    page.update()
