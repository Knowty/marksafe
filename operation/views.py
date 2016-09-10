from django.shortcuts import render
from django.views.generic.edit import FormView

from operation.forms import OperationCreateForm
from operation.models import Operation


class OperationCreateView(FormView):
    """
    This will handle creation of Refugees.
    """
    template_name = 'operation/create.html'
    form_class = OperationCreateForm
    success_url = '/victim/success'

    def form_valid(self, form):
        data = form.data.dict()
        data.pop('csrfmiddlewaretoken')
        Operation.objects.create(**data)
        return super(OperationCreateView, self).form_valid(form)
