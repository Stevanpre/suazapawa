from django.shortcuts import  get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from noticias.models import *
from noticias.forms import NoticiaForm
from eventos.models import *
from eventos.forms import EventoForm
from web.models import ImagenGaleria
from web.forms import ImagenGaleriaForm
from AmbienteEescolar.models import AmbienteCategoria, AmbienteImagen
from AmbienteEescolar.forms import AmbienteCategoriaForm, AmbienteImagenForm

# --------------------
# 🧭 Vista Principal del Panel Administrativo
# --------------------

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/modulos/bienvenida.html'  # por defecto carga bienvenida extendiendo dashboard
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        # decidir qué módulo mostrar según parámetro ?m=
        modulo = request.GET.get('m', 'bienvenida')
        # mapa de módulos a plantillas
        plantilla_map = {
            'bienvenida': 'admin/modulos/bienvenida.html',
            'perfil': 'admin/modulos/perfil.html',
            'calendario': 'admin/modulos/eventos.html',
            'noticias': 'admin/modulos/noticias.html',
            'galeria': 'admin/modulos/galeria.html',
            'ambiente_escolar': 'admin/modulos/ambiente_escolar.html',
        }
        self.template_name = plantilla_map.get(modulo, 'admin/modulos/bienvenida.html')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        modulo = self.request.GET.get('m', 'bienvenida')
        context['selected_module'] = modulo

        # Eventos
        eventos = Evento.objects.all().order_by('-fecha')
        context['eventos'] = eventos
        evento_id = self.request.GET.get('edit')
        if evento_id:
            evento = get_object_or_404(Evento, id=evento_id)
            context['form'] = EventoForm(instance=evento)
            context['modo_edicion'] = True
            context['evento_id'] = evento.id
            context['selected_module'] = 'calendario'
        else:
            context['form'] = EventoForm()

        # Noticias
        noticias = Noticia.objects.all().order_by('-fecha')
        context['noticias'] = noticias
        noticia_id = self.request.GET.get('edit_noticia')
        if noticia_id:
            noticia = get_object_or_404(Noticia, id=noticia_id)
            context['noticia_form'] = NoticiaForm(instance=noticia)
            context['modo_edicion_noticia'] = True
            context['noticia_id'] = noticia.id
            context['selected_module'] = 'noticias'
        else:
            context['noticia_form'] = NoticiaForm()

        # Galería
        imagenes = ImagenGaleria.objects.all()
        context['imagenes_galeria'] = imagenes
        imagen_id = self.request.GET.get('edit_imagen')
        if imagen_id:
            imagen = get_object_or_404(ImagenGaleria, id=imagen_id)
            context['galeria_form'] = ImagenGaleriaForm(instance=imagen)
            context['modo_edicion_imagen'] = True
            context['imagen_id'] = imagen.id
            context['selected_module'] = 'galeria'
        else:
            context['galeria_form'] = ImagenGaleriaForm()

        # Ambiente Escolar
        categorias = AmbienteCategoria.objects.all().order_by('orden')
        context['categorias_ambiente'] = categorias
        categoria_id = self.request.GET.get('edit_cat')
        if categoria_id:
            categoria = get_object_or_404(AmbienteCategoria, id=categoria_id)
            context['ambiente_cat_form'] = AmbienteCategoriaForm(instance=categoria)
            context['modo_edicion_cat'] = True
            context['categoria_id'] = categoria.id
            context['selected_module'] = 'ambiente_escolar'
        else:
            context['ambiente_cat_form'] = AmbienteCategoriaForm()

        imagenes_ambiente = AmbienteImagen.objects.select_related('categoria').all()
        context['imagenes_ambiente'] = imagenes_ambiente
        imagen_amb_id = self.request.GET.get('edit_amb_img')
        if imagen_amb_id:
            imagen_amb = get_object_or_404(AmbienteImagen, id=imagen_amb_id)
            context['ambiente_img_form'] = AmbienteImagenForm(instance=imagen_amb)
            context['modo_edicion_amb_img'] = True
            context['imagen_amb_id'] = imagen_amb.id
            context['selected_module'] = 'ambiente_escolar'
        else:
            context['ambiente_img_form'] = AmbienteImagenForm()

        # Métricas
        context['num_eventos'] = eventos.count()
        context['num_noticias'] = noticias.count()
        context['num_imagenes'] = imagenes.filter(publicada=True).count()
        context['num_ambiente'] = imagenes_ambiente.filter(publicada=True).count()
        context['ingresos_usuario'] = 80
        return context
