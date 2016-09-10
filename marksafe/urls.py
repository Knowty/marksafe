from django.conf.urls import include, url
from django.contrib import admin
from marksafe.forms import LoginForm
from marksafe.views import Home
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', views.logout,
                          {'next_page': '/'}),
    url(r'^$', Home.as_view()),
    url(r'refugee/', include('refugee.urls'))
]
