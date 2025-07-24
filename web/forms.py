from django import forms
from .models import Evento, Noticia
import datetime

# Clases reutilizables (Tailwind + DaisyUI + accesibilidad)
input_css = 'input input-bordered w-full text-sky-900 bg-white border-cyan-200 focus:ring-2 focus:ring-sky-300 transition'
textarea_css = 'textarea textarea-bordered w-full text-sky-900 bg-white border-cyan-200 focus:ring-2 focus:ring-sky-300 transition'

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': input_css,
                'placeholder': 'Título del evento',
                'required': True,
                'maxlength': 100,
                'aria-label': 'Título del evento'
            }),
            'fecha': forms.DateInput(attrs={
                'type': 'date',
                'min': datetime.date.today().isoformat(),
                'class': input_css,
                'required': True,
                'id': 'id_fecha',
                'aria-label': 'Fecha del evento'
            }),
            'hora': forms.TimeInput(attrs={
                'type': 'time',
                'class': input_css,
                'required': True,
                'aria-label': 'Hora del evento'
            }),
            'lugar': forms.TextInput(attrs={
                'class': input_css,
                'placeholder': 'Lugar del evento',
                'required': True,
                'aria-label': 'Lugar del evento'
            }),
            'descripcion_corta': forms.TextInput(attrs={
                'class': input_css,
                'placeholder': 'Descripción corta',
                'maxlength': 120,
                'aria-label': 'Descripción corta'
            }),
            'descripcion_detallada': forms.Textarea(attrs={
                'class': textarea_css,
                'rows': 5,
                'placeholder': 'Describe los detalles del evento...',
                'aria-label': 'Descripción detallada del evento'
            }),
        }


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': input_css,
                'placeholder': 'Título de la noticia',
                'required': True,
                'maxlength': 100,
                'aria-label': 'Título de la noticia'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': textarea_css,
                'rows': 4,
                'placeholder': 'Contenido de la noticia...',
                'required': True,
                'aria-label': 'Descripción de la noticia'
            }),
            'fecha': forms.DateInput(format='%Y-%m-%d', attrs={
                'type': 'date',
                'class': input_css,
                'required': True,
                'min': datetime.date.today().isoformat(),
                'aria-label': 'Fecha de la noticia'
            }),
            'hora': forms.TimeInput(format='%H:%M', attrs={
                'type': 'time',
                'class': input_css,
                'required': True,
                'aria-label': 'Hora de la noticia'
            }),
        }
