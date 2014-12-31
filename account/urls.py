from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'profile/$', 'account.views.profile_view'),
    url(r'dashboard/$', 'account.views.dashboard_view'),
)
