from indigo.settings import *


INSTALLED_APPS = (
    'indigo_bylaws',
) + INSTALLED_APPS + (
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
)

if DEBUG:
    INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)
    INSTALLED_APPS = INSTALLED_APPS + ('django_extensions',)
    MIDDLEWARE = MIDDLEWARE + ('debug_toolbar.middleware.DebugToolbarMiddleware',)


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
