from django.conf import settings
from django.conf.urls import include, url

from indigo.urls import urlpatterns


urlpatterns = [
    url(r'', include('indigo_workflow.urls', namespace='workflow')),
] + urlpatterns

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
