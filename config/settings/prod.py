from .base import *


ALLOWED_HOSTS = [
	
	'*'
]

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('apps/db.sqlite3'),
    }
}
