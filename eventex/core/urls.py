# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('eventex.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contato', name='contato'),
    url(r'^sobre/$', 'sobre', name='sobre'),
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', 'speaker_detail', name='speaker_detail'),
    url(r'^palestras/$', 'talk_list', name='talk_list'),
    # url(r'^(.+)/$', 'template_view', name='tpl'),
)