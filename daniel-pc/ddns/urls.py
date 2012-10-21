from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    # ex: /app/
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.redirect, name='index'),
    # ex: /app/create/
    url(r'^addip/$', views.addip, name='addip'),
    url(r'^redirect/$', views.redirect, name='redirect'),
    url(r'^createuser/$', views.createuser, name='createuser'),
)
