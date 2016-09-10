from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from refugee.models import Refugee


class RefugeeCreateView(CreateView):
    """
    This will handle creation of Refugees.
    """
    template_name = 'refugee/create.html'
    model = Refugee
    fields = ['name', 'phone_number', 'photo', 'notification_contact_number', 'location']
    success_url = '/refugee/success'


class RefugeeSearchView(View):
    """
    This will handle Refugee search.
    """

    def get(self, request):

        type = 'search'
        result = None

        if 'search_input' in request.GET:
            search_input = request.GET.get('search_input')
            type = 'result'

            #  Try to find a Refuge by name / number
            try:
                result = Refugee.objects.get(phone_number=search_input)
            except Refugee.DoesNotExist:
                result = None

        payload = {
            'type': type,
            'result': result
        }
        return render(request, 'refugee/search.html', payload)
