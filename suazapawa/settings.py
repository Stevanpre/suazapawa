from pathlib import Path
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Base directory del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta y debug desde .env
SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-insegura-defecto')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Hosts permitidos
ALLOWED_HOSTS = ['*']  # Para desarrollo y Railway

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web.apps.WebConfig',          # Tu app principal
    'axes',                        # Protección contra intentos fallidos
    'widget_tweaks',               # Para personalizar formularios en templates
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Sirve archivos estáticos en producción
    'axes.middleware.AxesMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs y WSGI
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

# Base de datos (SQLite para prototipo)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validaciones de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Archivos de medios (imagenes subidas)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Archivos estáticos (CSS, JS, imágenes)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'web/static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuración de login y sesión
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 1500  # 25 minutos
SESSION_SAVE_EVERY_REQUEST = True

# Backends de autenticación (incluye django-axes)
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Configuración de django-axes
AXES_FAILURE_LIMIT = 3
AXES_COOLOFF_TIME = 5  # minutos
AXES_RESET_ON_SUCCESS = True
AXES_LOCK_OUT_AT_FAILURE = True
AXES_LOCKOUT_TEMPLATE = 'auth/bloqueado.html'

# Internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Campo de clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

