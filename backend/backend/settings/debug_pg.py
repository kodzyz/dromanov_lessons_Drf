from .debug import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'library',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '54328',
    }
}

# pip install psycopg2-binary

# python manage.py runserver --settings=backend.settings.debug_pg
# python manage.py migrate --settings=backend.settings.debug_pg
# python manage.py createsuperuser --settings=backend.settings.debug_pg
