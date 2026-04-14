from utils.registry import VIEW_REGISTRY

def view(route):
    """
    Decorator to register a view.
    Associates the given route with the module and class name in the global registry.
    """
    def decorator(cls):
        VIEW_REGISTRY[route] = (cls.__module__, cls.__name__)
        return cls
    return decorator
