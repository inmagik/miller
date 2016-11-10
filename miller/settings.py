"""
Django settings for miller project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os, sys
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

management_command = sys.argv[1] if len(sys.argv) > 1 else ""
TESTING = management_command.startswith("test")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^gobax#cw-&*8i_lj*1(irdn-_pe4+qe5^5##+psz42mw$&c63'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

APPEND_SLASH = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'social.apps.django_app.default',
    'channels',
    'rest_framework',
    'djoser',
    'ws4redis',
    'simplemde',

    'miller'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'miller.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'client')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                # 'django.core.context_processors.static',
                'ws4redis.context_processors.default',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'miller.wsgi.application'

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'client/src'),
]

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME':  os.path.join(BASE_DIR, 'test.db.sqlite3'),
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization. Restrict the list of availble language for the website.
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('fr-fr', _('French'), 'fr_FR'),
    ('de-de', _('German'), 'de_DE'),
    ('en-us', _('English'), 'en_US'),
]


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 4
}

SIMPLEMDE_OPTIONS = {
    'autosave': {
        'enabled': True
    },
    
    'spellChecker': False
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL  = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'dist')
MEDIA_URL   = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

GIT_ROOT = os.path.join(BASE_DIR, 'contents')
GIT_COMMITTER = {
    'name': "A committer", 
    'email': "committer@example.com"
}

PROFILE_PATH_ROOT = os.path.join(GIT_ROOT, 'users')

PAGES_ROOT = os.path.join(BASE_DIR, 'client', 'pages')

SITE_ID=1

#............
#
# SOCIAL AUTH
#
#............
LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_USER_MODEL = 'auth.User'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'email']
SOCIAL_AUTH_UUID_LENGTH = 16
# override these settings in your local_settings.py file, cfr. http://psa.matiasaguirre.net/docs/configuration/settings.html
AUTHENTICATION_BACKENDS = (
  #'social.backends.google.GoogleOAuth2',
  # 'social.backends.twitter.TwitterOAuth',
  'django.contrib.auth.backends.ModelBackend',
)

#............
#
# WHOOSH
#
#............
WHOOSH_ROOT = os.path.join(BASE_DIR, 'whoosh')

#............
#
# RSS
#
#............
RSS_TITLE = 'Miller'
RSS_DESCRIPTION = 'Miller description'

#............
#
# REDIS
#
#............
WEBSOCKET_URL = '/ws/'
WS4REDIS_EXPIRE = 7200
WS4REDIS_PREFIX = 'miller'
# If the Redis datastore uses connection settings other than the defaults, use this dictionary to override these values
# WS4REDIS_CONNECTION = {
#     'host': 'localhost',
#     'port': 16379,
#     'db': 17,
#     'password': 'verysecret', # override these settings in your local_settings.py file
# }

#............
#
# LOGGING
#
#............
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'debug.log'),
            'formatter': 'lite'
        },
        'commands': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'commands.log'),
            'formatter': 'lite'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'lite':{
            'format': '%(levelname)s - %(asctime)s - %(module)s:%(lineno)s - %(funcName)20s - %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'miller.commands': {
            'handlers': ['console','commands'],
            'level': 'DEBUG'
        },
        'miller': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

#............
#
# Django channels
#
#............
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
        "ROUTING": "miller.routing.channel_routing",
    },
}

#............
#
# CODEMIRROR PLUGIN ADMIN
#
#............

CODEMIRROR_PATH = r'js/codemirror'
#............
#
# MILLER APP
#
#............


MILLER_DEBUG = True

MILLER_TITLE = 'RESuME'

MILLER_TEX = os.path.join(BASE_DIR, 'miller.tex')
# feel free to add your own oembed service in localsettings.
MILLER_OEMBEDS = {
  'vimeo':  {
    'endpoint': 'https://vimeo.com/api/oembed.json'
  }
}

MILLER_SETTINGS = {
  'debug': MILLER_DEBUG,
  'disqus': '',
  'socialtags': 'resume-unilu' # socila tags when sharing on twitter
}



# the settings above are the generic ones. Shall you need to change something, override the default values in a local_settings.py file instead.
try:
    from local_settings import *
except ImportError:
    pass
