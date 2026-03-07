from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from noticias.models import *
from eventos.models import Evento

# --------------------
# 📦 Páginas públicas
# --------------------

class navbarView(TemplateView):
    template_name = "public/includes/navbar.html"

class footerView(TemplateView):
    template_name = "public/includes/footer.html"

class HomeView(TemplateView):
    template_name = 'public/home.html'
    success_url   = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['eventos']  = Evento.objects.order_by('-fecha')[:3]
        ctx['noticias'] = Noticia.objects.order_by('-fecha')[:6]
        return ctx


# --------------------
# 📅 Calendario y Noticias pagina principal
# --------------------
class calendarioView(ListView):
    model = Evento
    template_name = "public/Nav/calendario.html"
    context_object_name = "eventos"
    ordering = ['fecha']

class TextoEscolarView(ListView):
    model = Noticia
    template_name = 'public/Nav/TextoEscolar.html'
    context_object_name = 'noticias'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        fecha = self.request.GET.get('fecha')
        orden = self.request.GET.get('orden')

        if query:
            queryset = queryset.filter(titulo__icontains=query)
        if fecha:
            queryset = queryset.filter(fecha=fecha)

        if orden == 'reciente':
            queryset = queryset.order_by('-fecha', '-hora')
        elif orden == 'antiguo':
            queryset = queryset.order_by('fecha', 'hora')
        else:
            queryset = queryset.order_by('-fecha', '-hora')

        return queryset


    #----------
    #  Bienestar Estudiantil
    #----------

class transporteView(TemplateView):
    template_name = 'public/bienestar/Transporte.html'

class restauranteView(TemplateView):
    template_name = 'public/bienestar/restaurante.html'

class enfermeriaView(TemplateView):
    template_name = 'public/bienestar/enfermeria.html'

class seguridadView(TemplateView):
    template_name = 'public/bienestar/seguridad.html'

#------------
# contacto
#------------
class admisionesView(TemplateView):
    template_name = 'public/contacto/admision.html'
class trabajaView(TemplateView):
    template_name = 'public/contacto/trabaja.html'
class contactoView(TemplateView):
    template_name = 'public/contacto/nosotros.html'


# --------------------
# 📌 Vistas institucionales
# --------------------

def somos(request): return render(request, 'public/ModNav/somos.html')
def mision(request): return render(request, 'public/ModNav/mision-vision.html')
def alumno(request): return render(request, 'public/ModNav/alumno.html')
def docente(request): return render(request, 'public/ModNav/docente.html')
def ubicacion(request): return render(request, 'public/ModNav/ubicacion.html')
