from django.urls import path
from . import views

urlpatterns = [
    path('ambiente/categoria/crear/', views.crear_categoria_ambiente, name='crear_categoria_ambiente'),
    path('ambiente/categoria/actualizar/<int:categoria_id>/', views.actualizar_categoria_ambiente, name='actualizar_categoria_ambiente'),
    path('ambiente/categoria/eliminar/<int:categoria_id>/', views.eliminar_categoria_ambiente, name='eliminar_categoria_ambiente'),
    path('ambiente/imagen/crear/', views.crear_imagen_ambiente, name='crear_imagen_ambiente'),
    path('ambiente/imagen/actualizar/<int:imagen_id>/', views.actualizar_imagen_ambiente, name='actualizar_imagen_ambiente'),
    path('ambiente/imagen/eliminar/<int:imagen_id>/', views.eliminar_imagen_ambiente, name='eliminar_imagen_ambiente'),
    path('ambiente/imagen/toggle/<int:imagen_id>/', views.toggle_publicar_imagen_ambiente, name='toggle_publicar_imagen_ambiente'),
]

