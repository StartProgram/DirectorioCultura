from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cultura',
        'USER': 'usercultura',
        'PASSWORD': 'cultura',
        'HOST': 'localhost',
        'PORT': '3306',
        'STORAGE_ENGINE': 'INNODB',
    }
}

STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR.child('media')

MEDIA_URL = '/media/'

STATICFILES_DIRS = [BASE_DIR.child('static')]

LOGIN_REDIRECT_URL = 'home:index'
