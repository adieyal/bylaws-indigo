from django.conf.urls import include, url
from django.views.generic import TemplateView

import indigo_social.views as views

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^terms', TemplateView.as_view(template_name='indigo_social/terms.html'), name='terms_of_use'),
    url('', include([
        # user edit pages
        url(r'^accounts/edit/$', views.EditAccountView.as_view(), name='edit_account'),
        url(r'^accounts/edit/api/$', views.EditAccountAPIView.as_view(), name='edit_account_api'),

        # profile page
        url(r'^users/(?P<pk>\d+)/$', views.UserProfileView.as_view(), name='user_profile'),
    ], 'indigo_social')),
]
