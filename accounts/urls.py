from django.conf.urls import include, url
from django.contrib.auth import views


urlpatterns = [
    url(r'^login/', views.login, {'template_name': 'login.html'})


]