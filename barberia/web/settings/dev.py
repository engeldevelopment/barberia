from .base import *


DEBUG = True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': dir_root('db.sqlite3'),
	}
}


STATICFILES_DIRS = [dir_root('static')]