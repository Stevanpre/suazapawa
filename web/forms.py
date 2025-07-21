from django import forms
from .models import Evento, Noticia

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full rounded-xl border border-cyan-200 bg-white px-4 py-2.5 text-base text-sky-900 shadow-sm focus:border-sky-400 focus:ring-2 focus:ring-sky-200 transition'
            }),
            'hora': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'w-full rounded-xl border border-cyan-200 bg-white px-4 py-2.5 text-base text-sky-900 shadow-sm focus:border-sky-400 focus:ring-2 focus:ring-sky-200 transition'
            }),
            'titulo': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-cyan-200 bg-white px-4 py-2.5 text-base text-sky-900 shadow-sm focus:border-sky-400 focus:ring-2 focus:ring-sky-200 transition'
            }),
            'descripcion_corta': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-cyan-200 bg-white px-4 py-2.5 text-base text-sky-900 shadow-sm focus:border-sky-400 focus:ring-2 focus:ring-sky-200 transition'
            }),
            'descripcion_detallada': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full rounded-xl border border-cyan-200 bg-white px-4 py-2.5 text-base text-sky-900 shadow-sm focus:border-sky-400 focus:ring-2 focus:ring-sky-200 transition'
            }),
            'lugar': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-cyan-200 bg-white px-4 py-2.5 text-base text-sky-900 shadow-sm focus:border-sky-400 focus:ring-2 focus:ring-sky-200 transition'
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-sm file:font-semibold file:bg-cyan-100 file:text-sky-700 hover:file:bg-cyan-200 transition'
            }),
        }

    def clean_descripcion_corta(self):
        data = self.cleaned_data['descripcion_corta']
        if len(data) > 10:
            raise forms.ValidationError("La descripción corta debe tener al menos 10 caracteres.")
        return data


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-cyan-200 bg-white px-4 py-2.5 text-base text-sky-900 shadow-sm focus:border-sky-400 focus:ring-2 focus:ring-sky-200 transition'
            }),
            'descripcion': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full rounded-xl border border-cyan-200 bg-white px-4 py-2.5 text-base text-sky-900 shadow-sm focus:border-sky-400 focus:ring-2 focus:ring-sky-200 transition'
            }),
            'fecha': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full rounded-xl border border-cyan-200 bg-white px-4 py-2.5 text-base text-sky-900 shadow-sm focus:border-sky-400 focus:ring-2 focus:ring-sky-200 transition'
            }),
            'hora': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'w-full rounded-xl border border-cyan-200 bg-white px-4 py-2.5 text-base text-sky-900 shadow-sm focus:border-sky-400 focus:ring-2 focus:ring-sky-200 transition'
            }),
        }
