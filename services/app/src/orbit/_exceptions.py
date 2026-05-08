class ViewNotFoundError(Exception):
    """Raised when the view for the specified route is not in the registry."""
    pass
