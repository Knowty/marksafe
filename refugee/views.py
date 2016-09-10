from django.shortcuts import render
from django.views.generic.edit import FormView

from refugee.forms import RefugeeCreateForm


class RefugeeCreateView(FormView):
    template_name = 'refugee/create.html'
    form_class = RefugeeCreateForm
    success_url = '/accounts/refugee-created-successfully'

