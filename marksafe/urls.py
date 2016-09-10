from django.conf.urls import include, url
from django.contrib import admin
from marksafe.forms import LoginForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('accounts.urls')),
    url(r'victim/', include('victim.urls')),
]
