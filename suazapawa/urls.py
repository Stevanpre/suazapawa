from django.contrib import admin
from django.urls import path
from web.views import *
from login.views import *
from noticias.views import *
from eventos.views import *
from perfil.views import *
from bienvenida.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

#------------Aplicaciones de la web----------------
    path('navbar/', navbarView.as_view(), name='navbar'),
    path('', HomeView.as_view(), name='home'),
    path('footer/', footerView.as_view(), name='footer'),


#------------Transportes, Restaurantes, Enfermeria, Seguridad----------------
    path('transporte/', transporteView.as_view(), name='transporte'),
    path('restaurante/', restauranteView.as_view(), name='restaurante'),
    path('enfermeria/', enfermeriaView.as_view(), name='enfermeria'),
    path('seguridad/',seguridadView.as_view(), name='seguridad'),

#------------Vistas de la web----------------
    path('calendario/', calendarioView.as_view(), name='calendario'),
    path('noticias/', TextoEscolarView.as_view(), name='textoescolar'),
    path('login/',UsuarioLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='home'), name='logout'),
   path('dashboard/', DashboardView.as_view(), name='dashboard'),
   path('bloqueado/', vista_bloqueado, name='bloqueado'),
    path('actualizar-perfil/', actualizar_perfil, name='actualizar_perfil'),

#------------URLs de la web----------------
path('somos/',somos, name='somos' ),
    path('mision/',mision, name='mision'),
    path('alumno/', alumno, name='alumno'),
    path('docente/', docente, name='docente'),
    path('ubicacion/', ubicacion, name='ubicacion'),

#------------Contacto-----------------
    path('admision/', admisionesView.as_view(), name='admision'),
    path('trabaja/', trabajaView.as_view(), name='trabaja'),
    path('contacto/', contactoView.as_view(), name='contacto'),


#------------web---------------
path('adminweb/', include('web.urls')),

#------------noticias---------------
    path('adminnoticias/', include('noticias.urls')),
#------------eventos---------------
    path('admineventos/', include('eventos.urls')),
#------------perfil---------------
    path('adminperfil/', include('perfil.urls')),
#------------bienvenida---------------
    path('adminbienvenida/', include('bienvenida.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
