

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Evento
from .models import Noticia
from django.db.models import Q

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

    def get_queryset(self):
        queryset = super().get_queryset()

        #--- FILTRO POR BUSQUEDA ---

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(titulo__icontains=query)

        #--- FILTRO POR FECHA ---
        fecha = self.request.GET.get('fecha')
        if fecha:
            queryset = queryset.filter(fecha=fecha)

        #--- ORDENAMIENTO ---

        orden = self.request.GET.get('orden')
        if orden == 'reciente':
            queryset = queryset.order_by('-fecha', '-hora')
        elif orden == 'antiguo':
            queryset = queryset.order_by('fecha', 'hora')
        else:
            queryset = queryset.order_by('-fecha', '-hora')

        return queryset



