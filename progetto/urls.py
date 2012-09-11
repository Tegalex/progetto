import os

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'progetto.views.home', name='home'),
    # url(r'^progetto/', include('progetto.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^%s(?P<path>.*)$'%settings.MEDIA_URL[1:],'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    #url(r'^admin/', )
    #url(r'^static/(?P<path>.*)$', include('static.urls')),
    #url(r'^media/(?P<path>.*)$', include('media.urls')),
)
urlpatterns += staticfiles_urlpatterns()
