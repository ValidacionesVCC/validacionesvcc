from django.contrib import admin
from django.urls import path, include
from core.views import convertir_pdf_en_imagenes_pdf

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página principal
    path('', include('core.urls')),

    # Login, register, logout
    path('app/', include('accounts.urls')),

    # API PDF → PDF imágenes
    path('api/convertir_pdf/', convertir_pdf_en_imagenes_pdf, name='convertir_pdf'),
]

