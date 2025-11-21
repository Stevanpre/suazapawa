from django.shortcuts import  redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import  Noticia
from .forms import NoticiaForm



# --------------------
# 📰 CRUD de Noticias administrativas
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