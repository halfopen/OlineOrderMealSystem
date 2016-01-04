from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OOMS.views.home', name='home'),
    # url(r'^OOMS/', include('OOMS.foo.urls')),


    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'home.views.index', name='home'),
    (r'^about/', 'home.views.about'),
    (r'^author/', 'home.views.author'),
    (r'^free_table', 'home.views.free_table'),
    (r'^export_excel/', 'home.views.export_excel'),
    (r'suggestion/$', 'suggestion.views.suggestion'),

    (r'^staff/', include('staff.urls')),
)
