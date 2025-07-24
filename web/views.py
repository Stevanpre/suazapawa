from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Evento, Noticia
from .forms import EventoForm, NoticiaForm
from django.db.models import Q

# --------------------
# 📦 Páginas públicas
# --------------------

def pruebas(request):
    return render(request, 'pruebas.html')

class navbarView(TemplateView):
    template_name = "public/includes/navbar.html"

class footerView(TemplateView):
    template_name = "public/includes/footer.html"

class HomeView(TemplateView):
    template_name = 'public/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Eventos ya existía
        context['eventos'] = Evento.objects.order_by('-fecha')[:3]
        # Añadimos las 3 noticias más recientes
        context['noticias'] = Noticia.objects.order_by('-fecha')[:3]
        return context


# --------------------
# 📅 Calendario y Noticias
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

# --------------------
# 🔐 Login & Dashboard
# --------------------

class UsuarioLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    def form_invalid(self, form):
        messages.error(self.request, "❌ Usuario o contraseña incorrectos.")
        return super().form_invalid(form)

def vista_bloqueado(request):
    return render(request, 'auth/bloqueado.html')

# --------------------
# 📌 Vistas institucionales
# --------------------

def somos(request): return render(request, 'public/ModNav/somos.html')
def mision(request): return render(request, 'public/ModNav/mision-vision.html')
def alumno(request): return render(request, 'public/ModNav/alumno.html')
def docente(request): return render(request, 'public/ModNav/docente.html')
def ubicacion(request): return render(request, 'public/ModNav/ubicacion.html')

# --------------------
# 🧭 Vista Principal del Panel Administrativo
# --------------------

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/dashboard.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 📅 Eventos
        eventos = Evento.objects.all().order_by('-fecha')
        context['eventos'] = eventos

        evento_id = self.request.GET.get('edit')
        if evento_id:
            evento = get_object_or_404(Evento, id=evento_id)
            context['form'] = EventoForm(instance=evento)
            context['modo_edicion'] = True
            context['evento_id'] = evento.id
        else:
            context['form'] = EventoForm()

        # 📰 Noticias
        noticias = Noticia.objects.all().order_by('-fecha')
        context['noticias'] = noticias

        noticia_id = self.request.GET.get('edit_noticia')
        if noticia_id:
            noticia = get_object_or_404(Noticia, id=noticia_id)
            context['noticia_form'] = NoticiaForm(instance=noticia)
            context['modo_edicion_noticia'] = True
            context['noticia_id'] = noticia.id
        else:
            context['noticia_form'] = NoticiaForm()

        # 📊 Métricas
        context['num_eventos'] = eventos.count()
        context['num_noticias'] = noticias.count()
        context['ingresos_usuario'] = 42

        return context



# --------------------
# 👤 Actualización de Perfil de Usuario
# --------------------

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
                update_session_auth_hash(request, user)
                messages.success(request, '✅ Contraseña actualizada correctamente.')
            else:
                messages.error(request, "❌ Las contraseñas no coinciden.")
                return redirect('dashboard')
        else:
            user.save()
            messages.success(request, '✅ Perfil actualizado correctamente.')

    return redirect('dashboard')

# --------------------
# 📆 CRUD de Eventos
# --------------------

@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Evento creado exitosamente.")
        else:
            messages.error(request, "❌ Error al crear el evento.")
    return redirect('dashboard')

@login_required
def actualizar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Evento actualizado correctamente.")
        else:
            messages.error(request, "❌ Error al actualizar el evento.")

    return redirect('dashboard')

@login_required
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    messages.success(request, "🗑 Evento eliminado correctamente.")
    return redirect('dashboard')

# --------------------
# 📰 CRUD de Noticias
# --------------------

@login_required
def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Noticia creada exitosamente.")
        else:
            messages.error(request, "❌ Error al crear la noticia.")
    return redirect('dashboard')

@login_required
def actualizar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)

    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Noticia actualizada correctamente.")
        else:
            messages.error(request, "❌ Error al actualizar la noticia.")

    return redirect('dashboard')

@login_required
def eliminar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    noticia.delete()
    messages.success(request, "🗑 Noticia eliminada correctamente.")
    return redirect('dashboard')
