from pathlib import Path
import os

# -------------------------------------------------------------------
# BASE DIR
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# SECURITY
# -------------------------------------------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "dev_key")

# DEBUG
DEBUG = os.getenv("RENDER") == ""

# Permitidos
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "www.validacionesvcc.com",
    "validacionesvcc.com",
    "validacionesvcc.onrender.com",
]

# -------------------------------------------------------------------
# SSL – solo en Render (EVITA LOOP INFINITO)
# -------------------------------------------------------------------
SECURE_SSL_REDIRECT = os.getenv("RENDER", "") != ""

# -------------------------------------------------------------------
# APPS
# -------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps del proyecto
    'accounts',
    'core',
]

# -------------------------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------------------------------------------------
# URL PRINCIPAL DEL PROYECTO
# -------------------------------------------------------------------
ROOT_URLCONF = 'proyecto1.urls'

# -------------------------------------------------------------------
# TEMPLATES
# -------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # carpeta global
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

# -------------------------------------------------------------------
# WSGI
# -------------------------------------------------------------------
WSGI_APPLICATION = 'proyecto1.wsgi.application'

# -------------------------------------------------------------------
# DATABASE
# -------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------------------------------------------------
# PASSWORD VALIDATION
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------------------------------------------
# LANGUAGE
# -------------------------------------------------------------------
LANGUAGE_CODE = 'es'

# -------------------------------------------------------------------
# TIMEZONE
# -------------------------------------------------------------------
TIME_ZONE = 'America/Bogota'

USE_I18N = True
USE_TZ = True

# -------------------------------------------------------------------
# STATIC FILES
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# ARCHIVOS ESTÁTICOS — FUNCIONA EN RENDER
# -------------------------------------------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"   # Render usará esto

# Siempre incluir carpeta /static/ del proyecto (aunque DEBUG esté en False)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Asegurar que Django indexe los archivos dentro de static/
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"


