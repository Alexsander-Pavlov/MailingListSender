"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os

from config.utils import find_env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = Path(__file__).resolve() / '.env'

load_dotenv(ENV_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i(7nvgjs=fiw$0*%qx3^!9-zgr0e0u%owrc+*$64^ysecc*amq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1']

CACHE_ENABLE = True
GLOBAL_CACHE = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    # celery
    'django_celery_beat',
    # debug_toolbar
    'debug_toolbar',
    # django-extensions
    'django_extensions',
    # phonenumber_field
    'phonenumber_field',
    'django_countries',
    # django-formset
    'formset',
    # custom apps
    'mess.apps.MessConfig',
    'users.apps.UsersConfig',
    'our_clients.apps.OurClientsConfig',
    'mail_center.apps.MailCenterConfig',
    'blog.apps.BlogConfig',
    'main_page.apps.MainPageConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # debug-toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

CELERY_IMPORTS = [
    'users.tasks'
]

if CACHE_ENABLE and GLOBAL_CACHE:
    MIDDLEWARE += [
        # global cache
        'django.middleware.cache.UpdateCacheMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
        ]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': find_env('DB_NAME'),
        'USER': find_env('DB_USER'),
        'HOST': find_env('DB_HOST'),
        'PASSWORD': find_env('DB_PASSWORD'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

if CACHE_ENABLE:
    match find_env('TEST'):
        case 'False':
            backend_cache = {
                'BACKEND': find_env('BACKEND_CACHE'),
                'LOCATION': find_env('LOCATION_CACHE'),
                'TIMEOUT': 60 * 10,
                'OPTIONS': {'db': '1'},
            }
        case _:
            backend_cache = {'BACKEND': find_env('BACKEND_CACHE_TEST')}
    CACHES = {'default': backend_cache}
    CACHE_MIDDLEWARE_KEY_PREFIX = 'messender_cache'
    CACHE_MIDDLEWARE_SECONDS = 600


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Omsk'

USE_I18N = True

USE_TZ = True

PHONENUMBER_DEFAULT_REGION = 'RU'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_CONNECT_TYPE = find_env('CONNECT_TYPE')

EMAIL_HOST = find_env('SMTP_EMAIL_HOST')
EMAIL_PORT = find_env('SMTP_EMAIL_PORT')
EMAIL_HOST_USER = find_env('HOST_USER')
EMAIL_HOST_PASSWORD = find_env('PASS_USER')
EMAIL_USE_SSL = True if EMAIL_CONNECT_TYPE == 'SSL' else False
EMAIL_USE_TLS = True if EMAIL_CONNECT_TYPE == 'TLS' else False

DEFAULT_CHARSET = 'utf-8'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

RMQ_HOST = find_env('RMQ_HOST')
RMQ_PORT = find_env('RMQ_PORT')
RMQ_USER = find_env('RABBITMQ_DEFAULT_USER')
RMQ_PASS = find_env('RABBITMQ_DEFAULT_PASS')

BROKER_URL = ('amqp://' +
              RMQ_USER +
              ':' +
              RMQ_PASS +
              '@' +
              RMQ_HOST +
              ':' +
              RMQ_PORT)

CELERY_BROKER_URL = BROKER_URL
CELERY_RESULT_BACKEND = 'redis://redis'
CELERY_RESULT_EXTENDED = True
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_BEAT_SCHEDULER = find_env('DEFAULT_DATABASE_BEAT')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = 'users:login'
LOGOUT_REDIRECT_URL = 'users:login'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'users.authentication.EmailAuthBackend',
]

AUTH_USER_MODEL = 'users.User'
