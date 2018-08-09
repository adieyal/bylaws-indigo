from django.conf.urls import include, url

import indigo_social.views as views

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url('', include([
        # user edit pages
        url(r'^accounts/edit/$', views.EditAccountView.as_view(), name='edit_account'),

        # profile page
        url(r'^users/(?P<pk>\d+)/$', views.UserProfileView.as_view(), name='user_profile'),
    ], 'indigo_social')),
]
