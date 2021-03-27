from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    '0.0.0.0',
    'localhost',
]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rss_db',
        'USER': 'rss_user',
        'PASSWORD': 'rss_pass',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "public/static"),
    ]
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media/')
MEDIA_URL = '/media/'