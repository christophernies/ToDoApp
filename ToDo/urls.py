from django.conf.urls import patterns, include, url
from todo_app.views import ToDo, CreateNewItem, DeleteItem, StoreClick, JSON_Emitter

urlpatterns = patterns('',
    url(r'^$', ToDo, name='home'),
    url(r'^list$', CreateNewItem),
    url(r'^delete$', DeleteItem),
    url(r'^record$', StoreClick),
    (r'^api/', include('api.urls')),
)
