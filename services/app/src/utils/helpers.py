from utils.loaders import get_view

def navigate(page, route):
    page.controls.pop()
    page.route = route
    ViewClass = get_view(route)
    view_instance = ViewClass()  # Instantiate the view
    page.controls.append(view_instance)
    page.update()  
