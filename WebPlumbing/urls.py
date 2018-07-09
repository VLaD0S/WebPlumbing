"""
Definition of urls for WebPlumbing.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from plumbing import views


from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    url(r'^', include('plumbing.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

   
]

#testcommit