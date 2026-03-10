from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

# --------------------
# 🔐 Login
# --------------------

class UsuarioLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Usuario o contraseña incorrectos.",
            extra_tags="error",
        )
        return super().form_invalid(form)

def vista_bloqueado(request):
    return render(request, 'auth/bloqueado.html')