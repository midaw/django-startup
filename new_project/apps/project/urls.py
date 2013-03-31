# -*- coding: utf-8 -*-
'''
Urls definition for this project (full site map).

When you crate new application, you need to do:
 - create copy of last "url(...)" statement
 - replace "new_app" to real name of your application.
 - uncomment this line (delete initial "#" symbol)
'''
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'apps.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    # copy this line for each new application that you have
    # url(r'^new_app/', include('apps.new_app.urls'), name='new_app'),
)