
from django.http import HttpResponse
#A middleware can be written as a function that looks like this:
def new_middleware(get_response):
    def middleware(request):
        print("Before MW1")
        response=get_response(request)
        
        print("After MW1")
        return response
    return middleware 

##Or it can be written as a class whose instances are callable, like this:
class NewMiddleware2:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before MW 2")
        response = self.get_response(request)
        print("After MW2")
        return response
    # In class-based middleware, process_view() is an optional hook method that Django calls just before the view function executes.
    # It lets you:
    # Inspect or modify the request
    # Short-circuit the process by returning a response early
    #Or just log / check data before the view runs
    def process_view(self, request, view_func, view_args, view_kwargs):
        print(">>> process_view called")
        print("View funct;ion:", view_func.__name__)
        print("View args:", view_args)
        print("View kwargs:", view_kwargs)
        #here i check if the student id is 100 it only then calls the view else just sends the reponse that this was blocked byt the middleware
        if view_kwargs.get('id') != 100:
            return HttpResponse("Access denied by middleware")


#middle ware cycle 

#client_request->middle_ware->view->model->middle_ware->response
#During the request phase, before calling the view, Django applies middleware in the order it’s defined in MIDDLEWARE, top-down.