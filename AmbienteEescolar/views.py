from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import AmbienteCategoria, AmbienteImagen
from .forms import AmbienteCategoriaForm, AmbienteImagenForm


def _redir_ambiente():
    return redirect(reverse('dashboard') + '?m=ambiente_escolar')


# --------------------
# 🏫 CRUD de Categorías (Dashboard)
# --------------------
@login_required
def crear_categoria_ambiente(request):
    if request.method == 'POST':
        form = AmbienteCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Categoría creada correctamente.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"❌ {field}: {error}")
    return _redir_ambiente()


@login_required
def actualizar_categoria_ambiente(request, categoria_id):
    categoria = get_object_or_404(AmbienteCategoria, id=categoria_id)
    if request.method == 'POST':
        form = AmbienteCategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Categoría actualizada correctamente.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"❌ {field}: {error}")
    return _redir_ambiente()


@login_required
def eliminar_categoria_ambiente(request, categoria_id):
    categoria = get_object_or_404(AmbienteCategoria, id=categoria_id)
    categoria.delete()
    messages.success(request, "🗑 Categoría eliminada correctamente.")
    return _redir_ambiente()


# --------------------
# 🖼️ CRUD de Imágenes (Dashboard)
# --------------------
@login_required
def crear_imagen_ambiente(request):
    if request.method == 'POST':
        form = AmbienteImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Imagen agregada al ambiente escolar.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"❌ {field}: {error}")
    return _redir_ambiente()


@login_required
def actualizar_imagen_ambiente(request, imagen_id):
    imagen = get_object_or_404(AmbienteImagen, id=imagen_id)
    if request.method == 'POST':
        form = AmbienteImagenForm(request.POST, request.FILES, instance=imagen)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Imagen actualizada correctamente.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"❌ {field}: {error}")
    return _redir_ambiente()


@login_required
def eliminar_imagen_ambiente(request, imagen_id):
    imagen = get_object_or_404(AmbienteImagen, id=imagen_id)
    imagen.imagen.delete(save=False)
    imagen.delete()
    messages.success(request, "🗑 Imagen eliminada correctamente.")
    return _redir_ambiente()


@login_required
def toggle_publicar_imagen_ambiente(request, imagen_id):
    imagen = get_object_or_404(AmbienteImagen, id=imagen_id)
    imagen.publicada = not imagen.publicada
    imagen.save()
    estado = "publicada" if imagen.publicada else "ocultada"
    messages.success(request, f"✅ Imagen {estado} correctamente.")
    return _redir_ambiente()
