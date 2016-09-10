from django.views.generic.edit import CreateView
from refugee.models import Refugee
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class RefugeeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'refugee/create.html'
    login_url = 'login/'
    model = Refugee
    fields = ['name', 'phone_number', 'photo', 'alternate_contact_number', 'location']
    success_url = '/refugee/success'
