import os
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================
# CONFIGURACIÓN BÁSICA
# ==========================

# En producción, Render te da SECRET_KEY por variable de entorno
SECRET_KEY = os.environ.get("SECRET_KEY", "cambia-esta-clave-en-produccion")

# DEBUG se controla por variable de entorno
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# Host externo de Render (ej: proteccion-pdf.onrender.com)
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS = [
        RENDER_EXTERNAL_HOSTNAME,
        ".onrender.com",
        "localhost",
        "127.0.0.1",
    ]
    CSRF_TRUSTED_ORIGINS = [f"https://{RENDER_EXTERNAL_HOSTNAME}"]
else:
    # Durante desarrollo local
    ALLOWED_HOSTS = ["*"]
    CSRF_TRUSTED_ORIGINS = []

# ==========================
# APLICACIONES INSTALADAS
# ==========================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # App donde pondremos la lógica de protección de PDF
    "core",
]

# ==========================
# MIDDLEWARE
# ==========================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ==========================
# URLS / WSGI
# ==========================

ROOT_URLCONF = "Proyecto_Proteccion_PDF.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Proyecto_Proteccion_PDF.wsgi.application"

# ==========================
# BASE DE DATOS (SQLite)
# ==========================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ==========================
# PASSWORDS / VALIDATORS
# ==========================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ==========================
# INTERNACIONALIZACIÓN
# ==========================

LANGUAGE_CODE = "es-co"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True

# ==========================
# ARCHIVOS ESTÁTICOS / MEDIA
# ==========================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ==========================
# CONFIG EXTRA PARA RENDER
# ==========================

# Para que Render respete HTTPS detrás de proxy
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
