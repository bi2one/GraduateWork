from django.conf.urls.defaults import *
from hospital import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^hospital/', include('hospital.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    # for index page
    (r'^$', 'hospital.page.views.index'),
    (r'^/$', 'hospital.page.views.index'),

    # (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       

    (r'^treatment/', include('hospital.treatment.urls')),
    (r'^admin/', include('hospital.admin.urls')),
    (r'^report/', include('hospital.report.urls')),
    (r'^page/', include('hospital.page.urls')),
    (r'^accounts/', include('hospital.accounts.urls')),
)
