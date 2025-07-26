from django import forms
from .models import Evento, Noticia, Contacto
import datetime
import bleach

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

    # Limpieza de campos para mayor seguridad
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '')
        return bleach.clean(titulo, tags=[], strip=True).strip()

    def clean_lugar(self):
        lugar = self.cleaned_data.get('lugar', '')
        return bleach.clean(lugar, tags=[], strip=True).strip()

    def clean_descripcion_corta(self):
        descripcion = self.cleaned_data.get('descripcion_corta', '')
        return bleach.clean(descripcion, tags=[], strip=True).strip()

    def clean_descripcion_detallada(self):
        descripcion = self.cleaned_data.get('descripcion_detallada', '')
        return bleach.clean(
            descripcion,
            tags=['b', 'i', 'u', 'a', 'ul', 'li'],
            attributes={'a': ['href', 'title']},
            strip=True
        ).strip()


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

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellido', 'email', 'telefono', 'mensaje']
        widgets = {
            'nombre':   forms.TextInput(attrs={
                            'class': input_css,
                            'placeholder': 'Tu nombre',
                            'required': True,
                            'maxlength': 50
                        }),
            'apellido': forms.TextInput(attrs={
                            'class': input_css,
                            'placeholder': 'Tu apellido',
                            'required': True,
                            'maxlength': 50
                        }),
            'email':    forms.EmailInput(attrs={
                            'class': input_css,
                            'placeholder': 'tu@correo.com',
                            'required': True
                        }),
            'telefono': forms.TextInput(attrs={
                            'class': input_css,
                            'placeholder': '+57 300 0000000',
                            'required': True,
                            'pattern': r'^\+?[0-9 ]{7,20}$',
                            'title': 'Sólo números y espacios, opcional +'
                        }),
            'mensaje':  forms.Textarea(attrs={
                            'class': textarea_css,
                            'placeholder': 'Tu mensaje...',
                            'required': True,
                            'rows': 4
                        }),
        }

    # Limpiamos para evitar XSS/inyecciones
    def clean_nombre(self):
        return bleach.clean(self.cleaned_data['nombre'], tags=[], strip=True).strip()

    def clean_apellido(self):
        return bleach.clean(self.cleaned_data['apellido'], tags=[], strip=True).strip()

    def clean_mensaje(self):
        return bleach.clean(self.cleaned_data['mensaje'], tags=[], strip=True).strip()
