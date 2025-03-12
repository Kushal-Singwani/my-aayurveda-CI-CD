from django.shortcuts import redirect
class RedirectIfLoggedInMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/login/' and request.user.is_authenticated:
            return redirect('home')  # Redirect to home page if logged in
        response = self.get_response(request)
        return response
