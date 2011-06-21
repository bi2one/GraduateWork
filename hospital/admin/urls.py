from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('hospital.admin.views',
    # Example:
    # (r'^hospital_service/', include('hospital_service.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    (r'request_patient/$', 'request_patient'),
    (r'request_caretaker/$', 'request_caretaker'),
    (r'request_message/$', 'request_message'),
    (r'request_executive/$', 'request_executive'),
                       
    (r'write_message/$', 'write_message'),
    # (r'api_test/$', 'api_test'),
)
