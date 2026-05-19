from django import forms
from .models import AmbienteCategoria, AmbienteImagen

field_input_css = 'field-input'


class AmbienteCategoriaForm(forms.ModelForm):
    class Meta:
        model = AmbienteCategoria
        fields = ['nombre', 'titulo_html', 'descripcion', 'icono', 'barra', 'publicada', 'orden']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': field_input_css,
                'placeholder': 'Nombre de la categoría',
                'maxlength': 80,
                'aria-label': 'Nombre',
            }),
            'titulo_html': forms.TextInput(attrs={
                'class': field_input_css,
                'placeholder': 'Título visible (puede usar <em>)',
                'maxlength': 120,
                'aria-label': 'Título',
            }),
            'descripcion': forms.TextInput(attrs={
                'class': field_input_css,
                'placeholder': 'Descripción de la sección',
                'maxlength': 240,
                'aria-label': 'Descripción',
            }),
            'icono': forms.TextInput(attrs={
                'class': field_input_css,
                'placeholder': 'Emoji o ícono',
                'maxlength': 8,
                'aria-label': 'Icono',
            }),
            'barra': forms.TextInput(attrs={
                'class': field_input_css,
                'placeholder': 'linear-gradient(...)',
                'maxlength': 140,
                'aria-label': 'Barra',
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


class AmbienteImagenForm(forms.ModelForm):
    class Meta:
        model = AmbienteImagen
        fields = ['categoria', 'titulo', 'imagen', 'descripcion', 'publicada', 'orden']
        widgets = {
            'categoria': forms.Select(attrs={
                'class': field_input_css,
                'aria-label': 'Categoría',
            }),
            'titulo': forms.TextInput(attrs={
                'class': field_input_css,
                'placeholder': 'Título de la imagen',
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

