from django.urls import path
from . import views
from .views import eliminar_correo

urlpatterns = [
    path('evento/crear/', views.crear_evento, name='crear_evento'),
    path('evento/editar/<int:evento_id>/', views.actualizar_evento, name='actualizar_evento'),
    path('evento/eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),


path('noticia/crear/', views.crear_noticia, name='crear_noticia'),
path('noticia/actualizar/<int:noticia_id>/', views.actualizar_noticia, name='actualizar_noticia'),
path('noticia/eliminar/<int:noticia_id>/', views.eliminar_noticia, name='eliminar_noticia'),

    path('eliminar-correo/', eliminar_correo, name='eliminar_correo'),

]
