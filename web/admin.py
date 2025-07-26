from django.contrib import admin
from .models import Evento
from .models import Noticia
from .models import Contacto

# Register your models here.

admin.site.register(Evento)
admin.site.register(Noticia)

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display    = ('nombre', 'apellido', 'email', 'telefono', 'creado_en')
    list_filter     = ('creado_en',)
    search_fields   = ('nombre', 'apellido', 'email', 'telefono')
    readonly_fields = ('creado_en',)
    ordering        = ('-creado_en',)
