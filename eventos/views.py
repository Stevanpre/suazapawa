from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Evento
from .forms import EventoForm

# --------------------
# 📆 CRUD de Eventos administrativos
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