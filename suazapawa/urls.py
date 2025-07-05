"""
URL configuration for suazapawa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import HomeView, calendarioView, TextoEscolarView, UsuarioLoginView, DashboardView, vista_bloqueado
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('calendario/', calendarioView.as_view(), name='calendario'),
    path('noticias/', TextoEscolarView.as_view(), name='textoescolar'),
    path('login/',UsuarioLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='home'), name='logout'),
   path('dashboard/', DashboardView.as_view(), name='dashboard'),
   path('bloqueado/', vista_bloqueado, name='bloqueado'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
