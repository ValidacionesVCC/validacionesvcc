from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ruta de tu página principal
    path('', include('core.urls')),

    # rutas de login / register / logout
    path('app/', include('accounts.urls')),
]
