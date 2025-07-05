

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Evento

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



