from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import CreateView, FormView

from operation.models import Operation
from processor.utils import push_record_to_sqs_queue
from victim.forms import RefugeeCreateForm
from victim.models import Victim

from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

# Create your views here.

class RefugeeCreateView(LoginRequiredMixin, FormView):
    """
    This will handle creation of Refugees.
    """
    template_name = 'victim/create.html'
    login_url = 'login/'
    form_class = RefugeeCreateForm
    success_url = '/victim/success'

    def form_valid(self, form):
        data = form.data.dict()
        data['operation'] = Operation.objects.get(id=data.get('operation'))
        data.pop('csrfmiddlewaretoken')
        Victim.objects.create(**data)
        return super(RefugeeCreateView, self).form_valid(form)



class RefugeeSearchView(LoginRequiredMixin, View):
    """
    This will handle Refugee search.
    """
    login_url = 'login/'
    def get(self, request):

        type = 'search'
        result = None

        if 'search_input' in request.GET:
            search_input = request.GET.get('search_input')
            type = 'result'

            #  Try to find a Refuge by name / number
            try:
                result = Victim.objects.get(phone_number=search_input)
            except Victim.DoesNotExist:
                result = None

        payload = {
            'type': type,
            'result': result
        }
        return render(request, 'victim/search.html', payload)
