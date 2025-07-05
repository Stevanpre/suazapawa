

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Evento
from .models import Noticia

# Create your views here.

class HomeView(TemplateView):
    template_name = "public/home.html"

class calendarioView(TemplateView):
    template_name = "public/calendario.html"

class calendarioView(ListView):
    model = Evento
    template_name = "public/calendario.html"
    context_object_name = "eventos"
    ordering = ['fecha']

class TextoEscolarView(ListView):
    model = Noticia
    template_name = 'public/TextoEscolar.html'
    context_object_name = 'noticias'
    ordering = ['fecha']


