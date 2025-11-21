from django.shortcuts import  get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
import os
from email.parser import Parser
from email.policy import default
import re
from noticias.models import *
from noticias.forms import NoticiaForm
from eventos.models import *
from eventos.forms import EventoForm

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
            'calendario': 'admin/modulos/calendario.html',
            'noticias': 'admin/modulos/noticias.html',
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
        # Métricas
        context['num_eventos'] = eventos.count()
        context['num_noticias'] = noticias.count()
        context['ingresos_usuario'] = 80
        # Correos
        correo_dir = os.path.join(settings.BASE_DIR, 'sent_emails')
        correos = []
        if os.path.exists(correo_dir):
            archivos = sorted(os.listdir(correo_dir), key=lambda x: os.path.getmtime(os.path.join(correo_dir, x)), reverse=True)
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
                        correos.append({'nombre': nombre_archivo,'contenido': datos_limpios})
                    except Exception as e:
                        correos.append({'nombre': nombre_archivo,'contenido': {'asunto': '[Error]', 'mensaje': f'No se pudo procesar: {e}'}})
        context['correos'] = correos
        return context
