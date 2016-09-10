from django import forms


class OperationCreateForm(forms.Form):
    name = forms.CharField(max_length=64)
    status = forms.CharField(max_length=20)