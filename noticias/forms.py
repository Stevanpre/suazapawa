
from django import forms
from .models import Noticia
import datetime
import bleach





# Clases reutilizables (Tailwind + DaisyUI + accesibilidad)
input_css = 'input input-bordered w-full text-sky-900 bg-white border-cyan-200 focus:ring-2 focus:ring-sky-300 transition'
textarea_css = 'textarea textarea-bordered w-full text-sky-900 bg-white border-cyan-200 focus:ring-2 focus:ring-sky-300 transition'

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

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '')
        return bleach.clean(titulo, tags=[], strip=True).strip()

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion', '')
        return bleach.clean(
            descripcion,
            tags=['b', 'i', 'u', 'a', 'ul', 'li'],
            attributes={'a': ['href', 'title']},
            strip=True
        ).strip()