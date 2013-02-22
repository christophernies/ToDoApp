from django.conf.urls import patterns, include, url
from todo_app.views import ToDo, CreateNewItem, DeleteItem, StoreClick, JSON_Emitter
from api.handlers import DataHandler

 # = Resource(DataHandler)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   # all my other url mappings
   (r'^api/', include('api.urls')),
   url(r'^data$', JSON_Emitter, { 'emitter_format': 'json' }),
)