from django.conf.urls import patterns, include, url
import trim
from trim import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', trim.views.home_view, name='home_view'),
    url(r'^(?P<trimmed_url>[a-z]{6})/$', trim.views.trimmed_url, name='trimmed_url'),
    url(r'^trim/$', trim.views.trim, name='trim'),
    url(r'^trim/(?P<trimmed_url>[a-z]{6})/$', trim.views.trimmed_url, name='trimmed_url'),
    # Examples:
    # url(r'^$', 'coffeeproject.views.home', name='home'),
    # url(r'^coffeeproject/', include('coffeeproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
