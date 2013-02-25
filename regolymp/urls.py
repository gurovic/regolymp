from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'regolymp.views.home', name='home'),
    # url(r'^regolymp/', include('regolymp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'contest.views.main', name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create_user$', 'contest.views.create_user', name='register'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html',}, name='login'),
)
