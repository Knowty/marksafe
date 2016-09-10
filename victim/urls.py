from django.conf.urls import url
from django.views.generic import TemplateView
from victim.views import RefugeeCreateView, RefugeeSearchView

urlpatterns = [
    url(r'^create$', RefugeeCreateView.as_view()),
    url(r'^search$', RefugeeSearchView.as_view()),
    url(r'^success$', TemplateView.as_view(template_name='refugee/created_successfully.html'))
]