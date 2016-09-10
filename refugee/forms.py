from django.forms import ModelForm

from refugee.models import Refugee


class RefugeeCreateForm(ModelForm):
    """
    Used to submit details about a refugee.
    """

    class Meta:
        model = Refugee
        exclude = ['safety_level']