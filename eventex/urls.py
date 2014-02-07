from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'eventex.core.views.home', name='home'),
    url(r'sobre/$', 'eventex.core.views.sobre', name='sobre'),
    url(r'contato/$', 'eventex.core.views.contato', name='contato'),
    url(r'^admin/', include(admin.site.urls)),
)
