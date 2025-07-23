

from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from pyexpat.errors import messages
from .models import Evento
from .models import Noticia
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import EventoForm, NoticiaForm
from django.shortcuts import get_object_or_404


# Create your views here.

def pruebas(request):
    return render(request, 'pruebas.html')

class navbarView(TemplateView):
    template_name = "public/includes/navbar.html"

class footerView(TemplateView):
    template_name = "public/includes/navbar.html"

class HomeView(TemplateView):
    template_name = "public/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.order_by('-fecha')[:3]
        context['noticias'] = Noticia.objects.order_by('-fecha')[:3]
        return context

class heroView(TemplateView):
    template_name = "public/SecHome/hero.html"

class nivelesView(TemplateView):
    template_name = "public/SecHome/nivelesAca.html"

class eventsView(TemplateView):
    template_name = "public/SecHome/eventos.html"

class experienciaView(TemplateView):
    template_name = "public/SecHome/exp.html"

class servicesView(TemplateView):
    template_name = "public/SecHome/servicios.html"

class galeriaView(TemplateView):
    template_name = "public/SecHome/galeria.html"

class noticesView(TemplateView):
    template_name = "public/SecHome/noticias.html"

class formularioView(TemplateView):
    template_name = "public/SecHome/formulario.html"


class calendarioView(TemplateView):
    template_name = "public/calendario.html"


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

class UsuarioLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    def form_invalid(self, form):
        messages.error(self.request, "❌ Usuario o contraseña incorrectos.")
        return super().form_invalid(form)

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/dashboard.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

def vista_bloqueado(request):
    return render(request, 'auth/bloqueado.html')

def somos(request):
    return render(request, 'public/ModNav/somos.html')

def mision(request):
    return render(request, 'public/ModNav/mision-vision.html')

def alumno(request):
    return render(request, 'public/ModNav/alumno.html')

def docente(request):
    return render(request, 'public/ModNav/docente.html')

def ubicacion(request):
    return render(request, 'public/ModNav/ubicacion.html')

@login_required
def actualizar_perfil(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')

        pwd1 = request.POST.get('password1')
        pwd2 = request.POST.get('password2')

        if pwd1:
            if pwd1 == pwd2:
                user.set_password(pwd1)
                user.save()
                update_session_auth_hash(request, user)  # 🔐 Evita cerrar sesión
                messages.success(request, 'Contraseña actualizada correctamente.')
            else:
                messages.error(request, "Las contraseñas no coinciden.")
                return redirect('dashboard')
        else:
            user.save()
            messages.success(request, 'Usuario actualizado correctamente.')

        return redirect('dashboard')


@login_required
def editar_calendario(request):
    eventos = Evento.objects.all().order_by('-fecha')
    form = EventoForm()
    return render(request, 'admin/modulos/calendario.html', {
        'form': form,
        'eventos': eventos
    })


@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Evento creado exitosamente.")
        else:
            messages.error(request, "❌ Error al crear el evento. Verifica los datos.")
    return redirect('dashboard')


@login_required
def actualizar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Evento actualizado correctamente.")
            return redirect('dashboard')
        else:
            messages.error(request, "❌ Hubo un error al actualizar el evento.")
    else:
        form = EventoForm(instance=evento)

    eventos = Evento.objects.all().order_by('-fecha')
    return render(request, 'admin/modulos/calendario.html', {
        'form': form,
        'eventos': eventos,
        'modo_edicion': True,
        'evento_id': evento.id
    })

@login_required
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    messages.success(request, "🗑 Evento eliminado correctamente.")
    return redirect('dashboard')




@login_required
def editar_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha')
    form = NoticiaForm()
    return render(request, 'admin/modulos/noticias.html', {
        'form': form,
        'noticias': noticias
    })

@login_required
def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Noticia creada exitosamente.")
        else:
            messages.error(request, "❌ Error al crear la noticia. Verifica los datos.")
    return redirect('dashboard')

@login_required
def actualizar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Noticia actualizada correctamente.")
            return redirect('dashboard')
        else:
            messages.error(request, "❌ Hubo un error al actualizar la noticia.")
    else:
        form = NoticiaForm(instance=noticia)

    noticias = Noticia.objects.all().order_by('-fecha')
    return render(request, 'admin/modulos/noticias.html', {
        'form': form,
        'noticias': noticias,
        'modo_edicion': True,
        'noticia_id': noticia.id
    })

@login_required
def eliminar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    noticia.delete()
    messages.success(request, "🗑 Noticia eliminada correctamente.")
    return redirect('dashboard')
