# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from models import *
from django.db.models import *
from datetime import timedelta, date
import json

list_of_items = [];
click_record = [];

# Create a new item, add it to the array used to store it, and render it
def CreateNewItem(request):
	if 'item' in request.GET:
		todo = request.GET['item']
	list_of_items.append(todo);
	return render_to_response('todo.html',{'list_of_items':list_of_items})

# Delete an item (currently only works after another item is added)
def DeleteItem(request):
	item = request.GET['item']
	list_of_items.remove(item);
	return render_to_response('todo.html')
	# return render_to_response('todo.html',{'list_of_items':list_of_items})

# Take the user's data from the javascript function that captured it and save it in the database
def StoreClick(request):
	click = request.GET['click']
	click_record.append(click)
	click = click.split(",")
	new_click = ClickData(click_date=click[1], click_time=click[2], click_url=click[0])
	new_click.save()
	return render_to_response('todo.html')
	# return render_to_response('todo.html',{'list_of_items':list_of_items})

# On opening the url (127.0.0.1:8000)
def ToDo(request):
	return render_to_response('todo.html')
	
# Displaying the JSON data
def JSON_Emitter(request, emitter_format):
	json_data = json.dumps(click_record, sort_keys=True, indent=4, separators=(',', ': '))
	return render_to_response('json.html',{"json":json_data})