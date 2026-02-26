from django.shortcuts import render
from .models import Flor
from django import forms


class FlorForm(forms.ModelForm):

    class Meta:
        model = Flor
        fields = '__all__'

        widgets = {

            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'rows': 4,
                'style': 'resize:none;'
}),

        }