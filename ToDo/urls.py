from django.conf.urls import patterns, include, url
from todo_app.views import ToDo, CreateNewItem, DeleteItem, StoreClick, JSON_Emitter
# from ToDo.api import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ToDo, name='home'),
    url(r'^list$', CreateNewItem),
    url(r'^delete$', DeleteItem),
    url(r'^record$', StoreClick),
    (r'^api/', include('api.urls')),
	url(r'^data(\.(?P<emitter_format>.+))$', JSON_Emitter),
    # url(r'^ToDo/', include('ToDo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
