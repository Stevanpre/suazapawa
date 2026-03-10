from django.contrib import admin
from .models import ImagenGaleria


@admin.register(ImagenGaleria)
class ImagenGaleriaAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'publicada', 'orden', 'fecha_subida')
    list_filter   = ('publicada',)
    search_fields = ('titulo', 'descripcion')
    ordering      = ('orden', '-fecha_subida')
    list_editable = ('publicada', 'orden')

