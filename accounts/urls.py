from django.conf.urls import include, url
from accounts.forms import LoginForm
from accounts.views import Signup
from django.contrib.auth import views
from victim.views import VictimSearchView

urlpatterns = [
    url(r'^$', VictimSearchView.as_view(), name='home'),
    url(r'^login/', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
    url(r'^signup/$', Signup.as_view()),
]