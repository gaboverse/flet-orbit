class ViewNotFoundError(Exception):
    """Exception raised when the view for the specified route is not found in the registry."""
    pass
