from django import forms
from datetime import datetime, date
import django
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.helpers import ActionForm

from surveys.models import Drug

class DrugForm(forms.ModelForm):
    """
    Form to create and edit template instance. 
    """

    class Meta:
        model = Drug
        fields = ["sample_text", "sample_bool"]