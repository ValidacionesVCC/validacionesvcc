# proyecto1/urls.py

from django.contrib import admin
from django.urls import path, include
from core.views import convertir_pdf_en_imagenes_pdf

urlpatterns = [
    # Panel admin
    path('admin/', admin.site.urls),

    # Rutas públicas (inicio, etc.)
    path('', include('core.urls')),

    # Rutas de la app de cuentas (login, registro, etc.)
    path('app/', include('accounts.urls')),

    # API para convertir PDF a PDF con imágenes (Power Automate)
    path('api/convertir_pdf/', convertir_pdf_en_imagenes_pdf, name='convertir_pdf'),
]
