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





MEDIA_URL = "/media/"

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATICFILES_DIRS = [BASE_DIR.child("static")]

MEDIA_ROOT = BASE_DIR.child("media")

LOGIN_REDIRECT_URL = 'home:home_user'

LOGOUT_REDIRECT_URL = 'home:index'