from .base import *

INTERNAL_IPS = ['127.0.0.1', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wis',
        'USER': 'wis_user',
        'PASSWORD': 'hellonepal',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DEBUG = True