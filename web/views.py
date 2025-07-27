from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Evento, Noticia
from .forms import EventoForm, NoticiaForm, ContactoForm
from django.core.mail import send_mail
from django.views.generic  import FormView
from django.conf import settings
import os
from django.views.decorators.csrf import csrf_exempt
from email.parser import Parser
from email.policy import default
import re

import datetime






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

class HomeView(FormView):
    template_name = 'public/home.html'
    form_class    = ContactoForm
    success_url   = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['eventos']  = Evento.objects.order_by('-fecha')[:3]
        ctx['noticias'] = Noticia.objects.order_by('-fecha')[:6]
        return ctx

    def form_valid(self, form):
        contacto = form.save()
        send_mail(
            subject=f"Nuevo mensaje de {contacto.nombre} {contacto.apellido}",
            message=(
                f"Nombre:  {contacto.nombre} {contacto.apellido}\n"
                f"Email:   {contacto.email}\n"
                f"Teléfono:{contacto.telefono}\n\n"
                f"Mensaje:\n{contacto.mensaje}"
            ),
            # usa DEFAULT_FROM_EMAIL
            from_email=None,
            recipient_list=['prueba@gmail.com'],
            fail_silently=False,
        )
        messages.success(self.request, "¡Gracias por escribirnos! Te responderemos pronto.")
        return super().form_valid(form)
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
# 🔐 Login
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
        context['ingresos_usuario'] = 80  # Ejemplo estático

        # 📬 Correos desde carpeta local "sent_emails"
        correo_dir = os.path.join(settings.BASE_DIR, 'sent_emails')
        correos = []

        if os.path.exists(correo_dir):
            archivos = sorted(
                os.listdir(correo_dir),
                key=lambda x: os.path.getmtime(os.path.join(correo_dir, x)),
                reverse=True
            )

            def extraer(patron, texto, flags=0):
                match = re.search(patron, texto, flags | re.IGNORECASE)
                return match.group(1).strip() if match else ''

            for nombre_archivo in archivos:
                if nombre_archivo.endswith('.log'):
                    ruta = os.path.join(correo_dir, nombre_archivo)
                    with open(ruta, encoding='utf-8') as f:
                        raw = f.read()

                    try:
                        email_message = Parser(policy=default).parsestr(raw)

                        if email_message.is_multipart():
                            body_part = email_message.get_body(preferencelist=('plain',))
                            body = body_part.get_content() if body_part else ''
                        else:
                            body = email_message.get_payload()

                        if not isinstance(body, str):
                            body = str(body)

                        datos_limpios = {
                            'asunto': email_message.get('Subject', ''),
                            'de': email_message.get('From', ''),
                            'para': email_message.get('To', ''),
                            'fecha': email_message.get('Date', ''),
                            'nombre': extraer(r"Nombre:\s*(.*)", body),
                            'email': extraer(r"Email:\s*(.*)", body),
                            'telefono': extraer(r"Tel[eé]fono:\s*(.*)", body),
                            'mensaje': extraer(r"Mensaje:\s*([\s\S]*)", body),
                        }

                        correos.append({
                            'nombre': nombre_archivo,
                            'contenido': datos_limpios,
                        })

                    except Exception as e:
                        correos.append({
                            'nombre': nombre_archivo,
                            'contenido': {
                                'asunto': '[Error al leer]',
                                'mensaje': f'No se pudo procesar el archivo: {e}'
                            }
                        })

        context['correos'] = correos
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


@csrf_exempt
@login_required
def eliminar_correo(request):
    if request.method == 'POST':
        archivo = request.POST.get('archivo')

        # Seguridad básica para evitar eliminar cualquier archivo arbitrario
        if not archivo.endswith('.log'):
            messages.error(request, "El archivo no es válido.")
            return redirect('dashboard')

        ruta = os.path.join(settings.BASE_DIR, 'sent_emails', archivo)  # Ajusta si usas otra carpeta

        if os.path.exists(ruta):
            os.remove(ruta)
            messages.success(request, f"Correo '{archivo}' eliminado exitosamente.")
        else:
            messages.error(request, "El archivo no existe.")

    return redirect('dashboard')
