from django import forms
from .models import ImagenGaleria

field_input_css = 'field-input'


class ImagenGaleriaForm(forms.ModelForm):
    class Meta:
        model = ImagenGaleria
        fields = ['titulo', 'imagen', 'descripcion', 'publicada', 'orden']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': field_input_css,
                'placeholder': 'Título de la imagen',
                'required': True,
                'maxlength': 100,
                'aria-label': 'Título',
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': field_input_css,
                'accept': 'image/*',
                'aria-label': 'Imagen',
            }),
            'descripcion': forms.TextInput(attrs={
                'class': field_input_css,
                'placeholder': 'Descripción corta (opcional)',
                'maxlength': 200,
                'aria-label': 'Descripción',
            }),
            'publicada': forms.CheckboxInput(attrs={
                'class': 'checkbox checkbox-primary',
                'aria-label': 'Publicada',
            }),
            'orden': forms.NumberInput(attrs={
                'class': field_input_css,
                'min': 0,
                'max': 999,
                'placeholder': '0',
                'aria-label': 'Orden',
            }),
        }

