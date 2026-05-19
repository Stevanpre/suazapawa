from django.contrib import admin
from .models import AmbienteCategoria, AmbienteImagen


@admin.register(AmbienteCategoria)
class AmbienteCategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'publicada', 'orden')
    list_filter = ('publicada',)
    search_fields = ('nombre', 'titulo_html', 'descripcion')
    ordering = ('orden', 'nombre')
    list_editable = ('publicada', 'orden')


@admin.register(AmbienteImagen)
class AmbienteImagenAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'publicada', 'orden', 'fecha_subida')
    list_filter = ('publicada', 'categoria')
    search_fields = ('titulo', 'descripcion')
    ordering = ('categoria', 'orden', '-fecha_subida')
    list_editable = ('publicada', 'orden')
