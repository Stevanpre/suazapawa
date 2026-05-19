from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from noticias.models import *
from eventos.models import Evento
from .models import ImagenGaleria
from .forms import ImagenGaleriaForm
from AmbienteEescolar.models import AmbienteCategoria
import json

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
        ctx['imagenes_galeria'] = ImagenGaleria.objects.filter(publicada=True)

        categorias_qs = AmbienteCategoria.objects.filter(publicada=True).order_by('orden')
        ambiente_cats = []
        for cat in categorias_qs:
            fotos_qs = cat.imagenes.filter(publicada=True).order_by('orden', '-fecha_subida')
            fotos = [
                {
                    'url': foto.imagen.url,
                    'title': foto.titulo,
                    'tag': foto.descripcion or cat.nombre,
                }
                for foto in fotos_qs
            ]
            if not fotos:
                continue
            ambiente_cats.append({
                'label': cat.titulo_html or cat.nombre,
                'desc': cat.descripcion,
                'icon': cat.icono or '🌿',
                'bar': cat.barra,
                'photos': fotos,
            })

        ctx['ambiente_cats'] = ambiente_cats
        ctx['ambiente_first'] = ambiente_cats[0] if ambiente_cats else None
        ctx['ambiente_cats_json'] = json.dumps(ambiente_cats)
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


# --------------------
# 🖼️  CRUD Galería (Dashboard)
# --------------------

def _redir_galeria():
    return redirect(reverse('dashboard') + '?m=galeria')


@login_required
def crear_imagen_galeria(request):
    if request.method == 'POST':
        form = ImagenGaleriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Imagen agregada a la galería.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"❌ {field}: {error}")
    return _redir_galeria()


@login_required
def actualizar_imagen_galeria(request, imagen_id):
    imagen = get_object_or_404(ImagenGaleria, id=imagen_id)
    if request.method == 'POST':
        form = ImagenGaleriaForm(request.POST, request.FILES, instance=imagen)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Imagen actualizada correctamente.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"❌ {field}: {error}")
    return _redir_galeria()


@login_required
def eliminar_imagen_galeria(request, imagen_id):
    imagen = get_object_or_404(ImagenGaleria, id=imagen_id)
    imagen.imagen.delete(save=False)   # elimina el archivo físico
    imagen.delete()
    messages.success(request, "🗑 Imagen eliminada de la galería.")
    return _redir_galeria()


@login_required
def toggle_publicar_imagen(request, imagen_id):
    """Alterna el estado publicada/oculta de una imagen."""
    imagen = get_object_or_404(ImagenGaleria, id=imagen_id)
    imagen.publicada = not imagen.publicada
    imagen.save()
    estado = "publicada" if imagen.publicada else "ocultada"
    messages.success(request, f"✅ Imagen {estado} correctamente.")
    return _redir_galeria()
