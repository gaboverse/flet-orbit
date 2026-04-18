import sys
from utils.registry import VIEW_REGISTRY
from utils.exceptions import ViewNotFoundError

def get_view(route):
    """
    Returns the view class associated with the given route using the global registry.
    Since all view modules are imported via ui/views/__init__.py, they are already loaded in sys.modules.
    """
    if route not in VIEW_REGISTRY:
        raise ViewNotFoundError(f"Route '{route}' not found in registry.")
    
    module_name, class_name = VIEW_REGISTRY[route]
    module = sys.modules.get(module_name)
    if module is None:
        raise ImportError(f"Module '{module_name}' not loaded.")
    view_class = getattr(module, class_name)
    return view_class
