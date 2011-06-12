from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('hospital.report.views',
    # Example:
    # (r'^hospital_service/', include('hospital_service.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    # (r'request_api/$', 'request_api'),
    (r'request_emergency/$', 'request_emergency'),
    (r'write_status/$', 'write_status'),
    (r'write_talk/$', 'write_talk'),
)
