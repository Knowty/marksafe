from django.conf.urls import url
from django.views.generic import TemplateView
from refugee.views import RefugeeCreateView

urlpatterns = [
    url(r'^create$', RefugeeCreateView.as_view()),
    url(r'^success$', TemplateView.as_view(template_name='refugee/created_successfully.html'))
]