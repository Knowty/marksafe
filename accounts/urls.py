from django.conf.urls import include, url
from accounts.forms import LoginForm
from accounts.views import Home
from django.contrib.auth import views
from victim.views import RefugeeCreateView, RefugeeSearchView

urlpatterns = [
    url(r'^$', RefugeeSearchView.as_view(), name='home'),
    url(r'^login/', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
]