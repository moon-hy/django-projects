from .base import *

ALLOWED_HOSTS = []

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {

            'level': 'DEBUG',
            'class': 'logging.StreamHandler',

        }

    },
    'loggers':{
        'django.db.backends':{
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_board',
        'USER': 'django_board',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = BASE_DIR / 'static/'

STATICFILES_DIRS = []
