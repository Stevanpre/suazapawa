from django.urls import path
from . import views

urlpatterns = [
    path('admision/',  views.enviar_admision,  name='enviar_admision'),
    path('contacto/',  views.enviar_contacto,  name='enviar_contacto'),
    path('trabaja/',   views.enviar_trabaja,   name='enviar_trabaja'),
]

