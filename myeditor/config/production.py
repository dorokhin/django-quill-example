from .base import *

ALLOWED_HOSTS += (
        'jan.dorokhin.moscow', 'dev.dorokhin.moscow'
    )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', None),
        'HOST': os.environ.get('POSTGRES_HOST', None),
        'USER': os.environ.get('POSTGRES_USER', None),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', None),
    },
}

MEDIA_ROOT = '/data/media'
STATIC_ROOT = '/data/static'
