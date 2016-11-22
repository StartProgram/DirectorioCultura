from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = '(iqjl0&8sf^&+naswc489p6z8j)k!=q014tq*mj5d=xxrfn@3k'


DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    )

THIRD_PARTY_APPS = (
    
    )

LOCAL_APPS = (
    'apps.artistas',
    'apps.eventos',
    'apps.tests',
    )

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ProyectoCultura.urls'

WSGI_APPLICATION = 'ProyectoCultura.wsgi.application'



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

TEMPLATE_DIRS = [BASE_DIR.child('templates')]



