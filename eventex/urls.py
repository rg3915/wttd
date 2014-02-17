# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('eventex.core.urls', namespace='core')),
    url(r'^inscricao/$', include('eventex.subscriptions.urls', namespace='subscription')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(.+)/$', 'eventex.core.views.template_view', name='tpl'),
)
