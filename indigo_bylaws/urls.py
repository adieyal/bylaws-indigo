from django.conf.urls import include, url

from indigo.urls import urlpatterns


urlpatterns = urlpatterns + [
    url(r'^accounts/', include('allauth.urls')),
]
