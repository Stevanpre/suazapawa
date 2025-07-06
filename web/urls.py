from django.urls import path
from . import views

urlpatterns = [
    path('evento/crear/', views.crear_evento, name='crear_evento'),
    path('evento/editar/<int:evento_id>/', views.actualizar_evento, name='actualizar_evento'),
    path('evento/eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
path('calendario/editar/', views.editar_calendario, name='editar_calendario'),

]
