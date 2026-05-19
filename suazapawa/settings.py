from pathlib import Path
import os
from dotenv import load_dotenv

# Cargar variables desde archivo .env
load_dotenv()

# BASE_DIR del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Modo desarrollo
DEBUG = True

# Clave secreta segura en entorno de desarrollo
SECRET_KEY = os.getenv('SECRET_KEY', 'clave-insegura-desarrollo')

# Hosts permitidos en entorno local
ALLOWED_HOSTS = ['*']

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web.apps.WebConfig',
    'eventos.apps.EventosConfig',
    'noticias.apps.NoticiasConfig',
    'bienvenida.apps.BienvenidaConfig',
    'perfil.apps.PerfilConfig',
    'login.apps.LoginConfig',
    'AmbienteEescolar.apps.AmbienteeescolarConfig',
    'axes',
    'widget_tweaks',
    'comunicaciones',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'axes.middleware.AxesMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLS
ROOT_URLCONF = 'suazapawa.urls'
WSGI_APPLICATION = 'suazapawa.wsgi.application'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'web/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Base de datos SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = []

# Archivos estáticos y media
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'web/static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuración de sesiones y login
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 1500
SESSION_SAVE_EVERY_REQUEST = True

# Backends de autenticación
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Configuración de django-axes
from datetime import timedelta
AXES_FAILURE_LIMIT = 3
AXES_COOLOFF_TIME = timedelta(minutes=5)
AXES_LOCKOUT_PARAMETERS = ['username']
AXES_RESET_ON_SUCCESS = True
AXES_LOCK_OUT_AT_FAILURE = True
AXES_LOCKOUT_TEMPLATE = 'auth/bloqueado.html'
AXES_HANDLER = 'axes.handlers.database.AxesDatabaseHandler'
AXES_IPWARE_PROXY_COUNT = 1
AXES_IPWARE_META_PRECEDENCE_ORDER = ['HTTP_X_FORWARDED_FOR', 'REMOTE_ADDR']

# ── Correo electrónico ──────────────────────────────────────────────────────
# Se usa SMTP real si EMAIL_HOST_USER está definido en .env, de lo contrario
# los correos se guardan como archivos en sent_emails/ (útil en desarrollo).
_email_user = os.getenv('EMAIL_HOST_USER', '')

if _email_user:
    EMAIL_BACKEND    = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST       = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_PORT       = int(os.getenv('EMAIL_PORT', 587))
    EMAIL_USE_TLS    = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
    EMAIL_HOST_USER  = _email_user
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
else:
    # Fallback: guarda los correos como archivos (desarrollo sin SMTP)
    EMAIL_BACKEND  = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'

DEFAULT_FROM_EMAIL    = os.getenv('DEFAULT_FROM_EMAIL', 'webmaster@localhost').strip("'\"")
CONTACT_EMAIL_DESTINO = os.getenv('CONTACT_EMAIL_DESTINO', 'marinonaranjoj@gmail.com')

# Logging — muestra errores de correo en la consola del servidor
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'comunicaciones': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.core.mail': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


# Internacionalización
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# Campo de clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
