from django.urls import path
from . import views

urlpatterns = [

path('noticia/crear/', views.crear_noticia, name='crear_noticia'),
path('noticia/actualizar/<int:noticia_id>/', views.actualizar_noticia, name='actualizar_noticia'),
path('noticia/eliminar/<int:noticia_id>/', views.eliminar_noticia, name='eliminar_noticia'),

]