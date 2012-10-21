from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    url(r'^', include('ddns.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
