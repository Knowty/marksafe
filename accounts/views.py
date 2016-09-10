from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

# Create your views here.

class Home(LoginRequiredMixin, View):
    template_name = "home.html"
    login_url = 'login/'
    def __init__(self, **kwargs):
        pass

    def get(self, request):
        # Only fetch students
        return render(request, self.template_name, {'users': {}, 'tasks': {}})