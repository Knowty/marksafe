from django.conf.urls import url
from operation.views import OperationCreateView

urlpatterns = [
    url(r'^create$', OperationCreateView.as_view()),
]