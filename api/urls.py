from django.conf.urls import patterns, include, url
from todo_app.views import ToDo, CreateNewItem, DeleteItem, StoreClick, JSON_Emitter
from api.handlers import DataHandler

urlpatterns = patterns('',
#URL Pattern to call the api: http://127.0.0.1:8000/api/
   url(r'^$', JSON_Emitter, { 'emitter_format': 'json' }),
)