from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'AlexGomez23$cultura',
        'USER': 'AlexGomez23',
        'PASSWORD': 'alexander',
        'HOST': 'AlexGomez23.mysql.pythonanywhere-services.com',
        'PORT': '',
        'STORAGE_ENGINE': 'INNODB',
    }
}





MEDIA_URL = "/media/"

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR.child("static")

MEDIA_ROOT = BASE_DIR.child("media")

LOGIN_REDIRECT_URL = 'home:home_user'

LOGOUT_REDIRECT_URL = 'home:index'