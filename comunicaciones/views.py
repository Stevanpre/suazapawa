from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import logging

logger = logging.getLogger(__name__)

DESTINO = getattr(settings, 'CONTACT_EMAIL_DESTINO', 'marinonaranjoj@gmail.com')


def _enviar_correo(asunto, cuerpo_html, adjuntos=None, reply_to=None):
    """Envía un correo al destinatario configurado y devuelve True/False."""
    try:
        # Gmail exige que from_email sea exactamente la cuenta autenticada
        from_email = settings.EMAIL_HOST_USER if hasattr(settings, 'EMAIL_HOST_USER') and settings.EMAIL_HOST_USER else settings.DEFAULT_FROM_EMAIL

        email = EmailMessage(
            subject=asunto,
            body=cuerpo_html,
            from_email=from_email,
            to=[DESTINO],
            reply_to=[reply_to] if reply_to else [],
        )
        email.content_subtype = 'html'
        if adjuntos:
            for nombre, contenido, mime in adjuntos:
                email.attach(nombre, contenido, mime)
        email.send(fail_silently=False)
        return True
    except Exception as e:
        logger.error(f"[CORREO] Error enviando '{asunto}': {type(e).__name__}: {e}")
        return False


# ────────────────────────────────────────────────────────────────────────────
# 📋  FORMULARIO DE ADMISIÓN
# ────────────────────────────────────────────────────────────────────────────
def enviar_admision(request):
    if request.method != 'POST':
        return redirect('admision')

    datos = {
        'nombre':   request.POST.get('nombre', '').strip(),
        'email':    request.POST.get('email', '').strip(),
        'telefono': request.POST.get('telefono', '').strip(),
        'grado':    request.POST.get('grado', '').strip(),
        'motivo':   request.POST.get('motivo', '').strip(),
    }

    # Validación básica
    if not all([datos['nombre'], datos['email'], datos['grado'], datos['motivo']]):
        messages.error(request, '❌ Por favor completa todos los campos obligatorios.')
        return redirect('admision')

    cuerpo = render_to_string('comunicaciones/email_admision.html', datos)
    asunto = f"📘 Nueva solicitud de admisión – {datos['nombre']}"
    ok = _enviar_correo(asunto, cuerpo, reply_to=datos['email'])

    if ok:
        messages.success(request,
            f"✅ ¡Gracias {datos['nombre']}! Tu solicitud fue enviada. Pronto nos pondremos en contacto contigo.")
    else:
        messages.error(request,
            '❌ Ocurrió un error al enviar el mensaje. Por favor intenta más tarde o escríbenos directamente.')

    return redirect('admision')


# ────────────────────────────────────────────────────────────────────────────
# 📬  FORMULARIO DE CONTACTO (nosotros)
# ────────────────────────────────────────────────────────────────────────────
def enviar_contacto(request):
    if request.method != 'POST':
        return redirect('contacto')

    datos = {
        'nombre':  request.POST.get('nombre', '').strip(),
        'email':   request.POST.get('email', '').strip(),
        'asunto':  request.POST.get('asunto', '').strip(),
        'mensaje': request.POST.get('mensaje', '').strip(),
    }

    if not all(datos.values()):
        messages.error(request, '❌ Por favor completa todos los campos obligatorios.')
        return redirect('contacto')

    cuerpo = render_to_string('comunicaciones/email_contacto.html', datos)
    asunto = f"📬 Contacto web – {datos['asunto']} ({datos['nombre']})"
    ok = _enviar_correo(asunto, cuerpo, reply_to=datos['email'])

    if ok:
        messages.success(request,
            f"✅ ¡Mensaje enviado, {datos['nombre']}! Te responderemos a {datos['email']} pronto.")
    else:
        messages.error(request,
            '❌ Ocurrió un error al enviar el mensaje. Por favor intenta más tarde.')

    return redirect('contacto')


# ────────────────────────────────────────────────────────────────────────────
# 💼  FORMULARIO TRABAJA CON NOSOTROS
# ────────────────────────────────────────────────────────────────────────────
def enviar_trabaja(request):
    if request.method != 'POST':
        return redirect('trabaja')

    datos = {
        'nombre':     request.POST.get('nombre', '').strip(),
        'email':      request.POST.get('email', '').strip(),
        'area':       request.POST.get('area', '').strip(),
        'telefono':   request.POST.get('telefono', '').strip(),
        'motivacion': request.POST.get('motivacion', '').strip(),
    }
    cv = request.FILES.get('cv')

    if not all([datos['nombre'], datos['email'], datos['area'], datos['motivacion']]):
        messages.error(request, '❌ Por favor completa todos los campos obligatorios.')
        return redirect('trabaja')

    adjuntos = []
    if cv:
        adjuntos.append((cv.name, cv.read(), cv.content_type))

    cuerpo = render_to_string('comunicaciones/email_trabaja.html', {**datos, 'tiene_cv': bool(cv)})
    asunto = f"💼 Solicitud laboral – {datos['area']} – {datos['nombre']}"
    ok = _enviar_correo(asunto, cuerpo, adjuntos=adjuntos, reply_to=datos['email'])

    if ok:
        messages.success(request,
            f"✅ ¡Gracias {datos['nombre']}! Tu hoja de vida fue enviada. Revisaremos tu perfil.")
    else:
        messages.error(request,
            '❌ Ocurrió un error al enviar el mensaje. Por favor intenta más tarde.')

    return redirect('trabaja')
