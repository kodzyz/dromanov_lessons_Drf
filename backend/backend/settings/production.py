from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'library',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'db',
        'PORT': '5432',
    }
}