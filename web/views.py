

from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from pyexpat.errors import messages

from .models import Evento
from .models import Noticia
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


# Create your views here.

class HomeView(TemplateView):
    template_name = "public/home.html"

class calendarioView(TemplateView):
    template_name = "public/calendario.html"

class calendarioView(ListView):
    model = Evento
    template_name = "public/calendario.html"
    context_object_name = "eventos"
    ordering = ['fecha']

class TextoEscolarView(ListView):
    model = Noticia
    template_name = 'public/TextoEscolar.html'
    context_object_name = 'noticias'

    def get_queryset(self):
        queryset = super().get_queryset()

        #--- FILTRO POR BUSQUEDA ---

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(titulo__icontains=query)

        #--- FILTRO POR FECHA ---
        fecha = self.request.GET.get('fecha')
        if fecha:
            queryset = queryset.filter(fecha=fecha)

        #--- ORDENAMIENTO ---

        orden = self.request.GET.get('orden')
        if orden == 'reciente':
            queryset = queryset.order_by('-fecha', '-hora')
        elif orden == 'antiguo':
            queryset = queryset.order_by('fecha', 'hora')
        else:
            queryset = queryset.order_by('-fecha', '-hora')

        return queryset
class UsuarioLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/dashboard.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

def vista_bloqueado(request):
    return render(request, 'auth/bloqueado.html')

@login_required
def actualizar_perfil(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')

        pwd1 = request.POST.get('password1')
        pwd2 = request.POST.get('password2')

        if pwd1:
            if pwd1 == pwd2:
                user.set_password(pwd1)
                user.save()
                update_session_auth_hash(request, user)  # 🔐 Evita cerrar sesión
                messages.success(request, 'Contraseña actualizada correctamente.')
            else:
                messages.error(request, "Las contraseñas no coinciden.")
                return redirect('dashboard')
        else:
            user.save()
            messages.success(request, 'Usuario actualizado correctamente.')

        return redirect('dashboard')
