from django.conf import settings
from django.conf.urls import include, url

from indigo.urls import urlpatterns


urlpatterns = urlpatterns + [
    url('', include('indigo_social.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns