from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', coffeeproject.trim.views.home_view, name='home_view'),
    url(r'^trim/$', coffeproject.trim.views.trim, name='trim'),
    url(r'^trim/(?P<trimmed_url>\d+)/$', coffeeproject.trim.views.trimmed_url, name='trimmed_url'),
    # Examples:
    # url(r'^$', 'coffeeproject.views.home', name='home'),
    # url(r'^coffeeproject/', include('coffeeproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
