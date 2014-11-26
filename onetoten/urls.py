from django.conf.urls import patterns, include, url
from django.contrib import admin

import dashboard, profile, user

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onetoten.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'onetoten.views.home'),
    url(r'^register/', 'onetoten.views.register'),


    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^profile/', include('profile.urls'))
)
