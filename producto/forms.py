import re
from django.core.exceptions import ValidationError
from django import forms
from .models import Producto

def validate_no_numeros(valor):
    if any(char.isdigit() for char in valor):
        raise ValidationError("Este campo no puede contener números.")

def validate_nombre(valor):
    if not valor or len(valor.strip()) < 3:
        raise ValidationError("El nombre debe tener al menos 3 caracteres.")
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', valor):
        raise ValidationError("El nombre solo puede contener letras y espacios.")
    validate_no_numeros(valor)

def validate_descripcion(valor):
    if not valor or len(valor.strip()) < 10:
        raise ValidationError("La descripción debe tener al menos 10 caracteres.")
    validate_no_numeros(valor)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre (solo letras)',
                'pattern': '[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+',
                'title': 'Solo se permiten letras y espacios'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'style': 'resize:none;',
                'placeholder': 'Descripción (solo letras, mín. 10 carac.)',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        validate_nombre(nombre)
        return nombre.strip()

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        validate_descripcion(descripcion)
        return descripcion.strip()

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is None or precio < 0:
            raise ValidationError("El precio no puede ser negativo ni estar vacío.")
        return precio

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is None or cantidad < 0:
            raise ValidationError("La cantidad no puede ser negativa ni estar vacía.")
        return cantidad