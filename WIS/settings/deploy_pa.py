from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wis',
        'USER': 'abhishekjung',
        'PASSWORD': 'hellonepal',
        'HOST': 'abhishekjung.mysql.pythonanywhere-services.com',
    }
}