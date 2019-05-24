from .base import *


ALLOWED_HOSTS = [
	
	'*'
]

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': dir_root('db.sqlite3'),
    }
}

STATIC_ROOT = dir_root('static')