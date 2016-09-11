from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.shortcuts import render
from accounts.models import User
from django.contrib.auth import login
from django.shortcuts import redirect

class Signup(View):
    template_name = "signup.html"
    def __init__(self, **kwargs):
        pass

    def get(self, request):
        # Only fetch students
        return render(request, self.template_name)
    
    def post(self, request):
        try:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            raw_password = request.POST.get("password")
            new_user = User.objects.create_user(email, first_name= first_name, last_name = last_name, email = email)
            new_user.set_password(raw_password)
            new_user.save()
            login(self.request, new_user)
        except:
            pass
        return redirect('/')