from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# ----------------------
# LOGIN
# ----------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # ESTA RUTA DEBE EXISTIR EN core/urls.py
            return redirect("inicio")

        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "accounts/login.html")


# ----------------------
# LOGOUT
# ----------------------
def logout_view(request):
    logout(request)

    # ESTA RUTA EXISTE EN accounts/urls.py
    return redirect("login")


# ----------------------
# REGISTER
# ----------------------
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Validación: usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
            return redirect("register")

        # Crear usuario
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Cuenta creada correctamente")
        return redirect("login")

    return render(request, "accounts/register.html")
