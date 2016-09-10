from django import forms

from operation.models import Operation
from refugee.models import Refugee, SAFETY_LEVELS


class RefugeeCreateForm(forms.Form):
    name = forms.CharField(max_length=64)
    phone_number = forms.CharField(max_length=20)
    photo = forms.ImageField(required=False)
    notification_contact_number = forms.CharField(max_length=20, required=False)
    location = forms.CharField(widget=forms.Textarea, required=False)
    comments = forms.CharField(widget=forms.Textarea, required=False)
    operation = forms.ModelChoiceField(queryset=Operation.objects.all(),  widget=forms.Select, empty_label=None)
