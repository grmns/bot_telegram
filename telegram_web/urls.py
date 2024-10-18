from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('botapp.urls')),  # Ruta de la app botapp

    # Incluir URLs predeterminadas de autenticación (login, logout, cambio de contraseña)
    path('accounts/', include('django.contrib.auth.urls')),

    # Ruta para el registro de usuarios
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
