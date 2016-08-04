from django.conf.urls import patterns, include, url
from django.contrib import admin
from practo.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practo_api_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^doctor/create', create_doctor),
    url(r'^clinic/create', create_clinic),
    url(r'doctor/search', search_doctor),
    url(r'clinic/search', search_clinic),
    url(r'doctor/update', update_doctor),
    url(r'clinic/update', update_clinic),
    url(r'doctor/delete', delete_doctor),
    url(r'clinic/delete', delete_clinic),
)
