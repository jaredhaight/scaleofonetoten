from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onetoten.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'onetoten.views.home'),
    url(r'^register/', 'onetoten.views.register_view'),
    url(r'^login/', 'onetoten.views.login_view'),
    url(r'^logout/', 'onetoten.views.logout_view'),
    url(r'^api/', include('api.urls')),
    url(r'^account/', include('account.urls'))
)
