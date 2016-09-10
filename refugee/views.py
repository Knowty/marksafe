from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import CreateView, FormView

from operation.models import Operation
from processor.utils import push_record_to_sqs_queue
from refugee.forms import RefugeeCreateForm
from refugee.models import Refugee


class RefugeeCreateView(FormView):
    """
    This will handle creation of Refugees.
    """
    template_name = 'refugee/create.html'
    form_class = RefugeeCreateForm
    success_url = '/refugee/success'

    def form_valid(self, form):
        data = form.data.dict()
        data['operation'] = Operation.objects.get(id=data.get('operation'))
        data.pop('csrfmiddlewaretoken')
        Refugee.objects.create(**data)
        return super(RefugeeCreateView, self).form_valid(form)



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
