from django import forms
from .models import Flor

class FlorForm(forms.ModelForm):
    class Meta:
        model = Flor
        fields = '__all__'