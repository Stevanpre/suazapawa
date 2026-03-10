from django.urls import path
from . import views

urlpatterns = [
    path('galeria/crear/', views.crear_imagen_galeria, name='crear_imagen_galeria'),
    path('galeria/actualizar/<int:imagen_id>/', views.actualizar_imagen_galeria, name='actualizar_imagen_galeria'),
    path('galeria/eliminar/<int:imagen_id>/', views.eliminar_imagen_galeria, name='eliminar_imagen_galeria'),
    path('galeria/toggle/<int:imagen_id>/', views.toggle_publicar_imagen, name='toggle_publicar_imagen'),
]
