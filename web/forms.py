from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_corta': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_detallada': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_descripcion_corta(self):
        data = self.cleaned_data['descripcion_corta']
        if len(data) < 10:
            raise forms.ValidationError("La descripción corta debe tener al menos 10 caracteres.")
        return data
