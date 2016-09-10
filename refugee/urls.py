from django.conf.urls import url

from refugee.views import RefugeeCreateView

urlpatterns = [
    url(r'^create$', RefugeeCreateView.as_view())
]