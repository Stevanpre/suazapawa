from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Evento
from .forms import EventoForm

# --------------------
# 📆 CRUD de Eventos administrativos
# --------------------

def _redir_calendario():
    return redirect(reverse('dashboard') + '?m=calendario')

@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Evento creado exitosamente.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"❌ {field}: {error}")
    return _redir_calendario()

@login_required
def actualizar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Evento actualizado correctamente.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"❌ {field}: {error}")
    return _redir_calendario()

@login_required
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    messages.success(request, "🗑 Evento eliminado correctamente.")
    return _redir_calendario()
