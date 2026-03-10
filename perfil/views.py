from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.urls import reverse

# --------------------
# 👤 Actualización de Perfil de Usuario
# --------------------

@login_required
def actualizar_perfil(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '').strip()
        user.username   = request.POST.get('username', '').strip()
        user.email      = request.POST.get('email', '').strip()

        pwd1 = request.POST.get('password1', '').strip()
        pwd2 = request.POST.get('password2', '').strip()

        if pwd1:
            if pwd1 == pwd2:
                user.set_password(pwd1)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, '✅ Contraseña actualizada correctamente.')
            else:
                messages.error(request, "❌ Las contraseñas no coinciden.")
                return redirect(reverse('dashboard') + '?m=perfil')
        else:
            user.save()
            messages.success(request, '✅ Perfil actualizado correctamente.')

    return redirect(reverse('dashboard') + '?m=perfil')
