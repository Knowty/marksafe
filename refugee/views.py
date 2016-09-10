from django.views.generic.edit import CreateView
from refugee.models import Refugee


class RefugeeCreateView(CreateView):
    template_name = 'refugee/create.html'
    model = Refugee
    fields = ['name', 'phone_number', 'photo', 'alternate_contact_number', 'location']
    success_url = '/refugee/success'