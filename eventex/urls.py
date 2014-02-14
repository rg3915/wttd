from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('eventex.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^(.+)/$', 'template_view', name='tpl'),
    url(r'^inscricao/$', 'eventex.subscriptions.views.subscribe', name='subscribe'),
    url(r'^admin/', include(admin.site.urls)),
)
