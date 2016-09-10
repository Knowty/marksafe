from django import forms

from operation.models import Operation
from victim.models import Victim, SAFETY_LEVELS


class VictimCreateForm(forms.Form):
    name = forms.CharField(max_length=64)
    phone_number = forms.CharField(max_length=20)
    notification_contact_number = forms.CharField(max_length=20, required=False)
    location = forms.CharField(widget=forms.Textarea, required=False)
    operation = forms.ModelChoiceField(queryset=Operation.objects.all(),  widget=forms.Select, empty_label=None)
