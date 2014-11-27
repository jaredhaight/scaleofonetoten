# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'onetoten',
        'USER': 'onetoten',
        'PASSWORD': os.environ["OTT_SQL_PASS"],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.environ["OTT_STATIC_PATH"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["OTT_SECRET_KEY"]

if os.environ["OTT_ENV"] == "DEV":
    DEBUG = True
    TEMPLATE_DEBUG = True