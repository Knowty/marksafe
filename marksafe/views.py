from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.shortcuts import render



class Home(View):
    template_name = "home.html"
    login_url = 'login/'
    def __init__(self, **kwargs):
        pass

    def get(self, request):
        # Only fetch students
        return render(request, self.template_name, {'users': {}, 'tasks': {}})