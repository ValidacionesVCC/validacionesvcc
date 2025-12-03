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
            return redirect("inicio")   # ← Asegúrate que esta ruta existe
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "accounts/login.html")


# ----------------------
# LOGOUT
# ----------------------
def logout_view(request):
    logout(request)
    return redirect('login')   # ← esta ruta debe existir en accounts/urls.py


# ----------------------
# REGISTER
# ----------------------
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Cuenta creada correctamente")
        return redirect("login")

    return render(request, "accounts/register.html")
