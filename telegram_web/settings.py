import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = 'django-insecure-m1m7nx8wg8mi#$apqcoep1!z(&ac$dhuhe7k-+_utt4zss#1jf'  # Mantenlo seguro en producción

# DEBUG: True para desarrollo
DEBUG = True

# Hosts permitidos (puedes cambiar esto si necesitas trabajar con hosts específicos)
ALLOWED_HOSTS = []

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'botapp',  # Agrega tu aplicación
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de URLs
ROOT_URLCONF = 'telegram_web.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Puedes agregar el directorio donde tienes tus plantillas si no están en las apps
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI para correr el servidor
WSGI_APPLICATION = 'telegram_web.wsgi.application'

# Base de datos (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bot_telegram',  # Nombre de tu base de datos
        'USER': 'grmn',  # Usuario de tu base de datos
        'PASSWORD': 'Grman72463758',  # Contraseña de tu base de datos
        'HOST': 'localhost',  # Dirección de tu base de datos
        'PORT': '5432',  # Puerto de tu base de datos
    }
}

# Autenticación
LOGIN_URL = '/accounts/login/'  # URL para el login
LOGIN_REDIRECT_URL = '/'  # URL después de iniciar sesión
LOGOUT_REDIRECT_URL = '/accounts/login/'  # URL después de cerrar sesión

# Archivos estáticos y de medios
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'

# Configuración de archivos estáticos en producción (localmente esto no es necesario)
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Para desarrollo local

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
