import os

from indigo.settings import *


INSTALLED_APPS = (
    'indigo_bylaws',
) + INSTALLED_APPS + (
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'elasticapm.contrib.django',
)

# Elasticsearch and logstash
LOGSTASH_URL = os.environ.get('LOGSTASH_URL', '')
APM_SERVER_URL = os.environ.get('APM_SERVER_URL', '')
ELK_PROJECT = 'indigo-bylaws'
ELASTIC_APM = {
    'SERVICE_NAME': ELK_PROJECT,
    'SERVER_URL': APM_SERVER_URL,
}

if DEBUG:
    INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)
    INSTALLED_APPS = INSTALLED_APPS + ('django_extensions',)
    MIDDLEWARE = MIDDLEWARE + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
else:
    MIDDLEWARE = MIDDLEWARE + (
        'elasticapm.contrib.django.middleware.TracingMiddleware',
        'elasticapm.contrib.django.middleware.Catch404Middleware',
    )
    LOGGING['handlers']['logstash'] = {
        'level': 'DEBUG',
        'class': 'logstash.TCPLogstashHandler',
        'host': LOGSTASH_URL,
        'port': 5959,
        'version': 1,
        'message_type': 'logstash',
        'fqdn': False,
        'tags': [ELK_PROJECT]
    }
    LOGGING['handlers']['elasticapm'] = {
        'level': 'INFO',
        'class': 'elasticapm.contrib.django.handlers.LoggingHandler',
    }


ROOT_URLCONF = 'indigo_bylaws.urls'


INTERNAL_IPS = ['127.0.0.1']


# Django all-auth settings
ACCOUNT_EMAIL_VERIFICATION = 'required'
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'picture',
            'gender',
        ],
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    },
}
