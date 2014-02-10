from .base import *

SECRET_KEY = 'ljsdghljsdglj'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}