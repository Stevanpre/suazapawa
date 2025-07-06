from django.urls import path
from . import views

urlpatterns = [
    path('evento/crear/', views.crear_evento, name='crear_evento'),
    path('evento/editar/<int:evento_id>/', views.actualizar_evento, name='actualizar_evento'),
    path('evento/eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
path('calendario/editar/', views.editar_calendario, name='editar_calendario'),


path('noticia/editar', views.editar_noticias, name='editar_noticias'),
path('noticia/crear/', views.crear_noticia, name='crear_noticia'),
path('noticia/actualizar/<int:noticia_id>/', views.actualizar_noticia, name='actualizar_noticia'),
path('noticia/eliminar/<int:noticia_id>/', views.eliminar_noticia, name='eliminar_noticia'),


]
