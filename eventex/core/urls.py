# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('eventex.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contato', name='contato'),
    url(r'^sobre/$', 'sobre', name='sobre'),
    # url(r'^(.+)/$', 'template_view', name='tpl'),
)