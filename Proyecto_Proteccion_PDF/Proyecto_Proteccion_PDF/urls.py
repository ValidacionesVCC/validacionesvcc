from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin estándar de Django (por si lo necesitas)
    path("admin/", admin.site.urls),

    # Endpoints de tu API de protección de PDF
    # Aquí asumimos que tendrás core/urls.py
    path("api/", include("core.urls")),
]
