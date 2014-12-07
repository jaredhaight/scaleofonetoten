from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^v1/sms/', 'api.views.sms'),
)
