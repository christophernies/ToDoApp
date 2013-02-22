ToDoApp
=======

Trying out some JSON API stuff.

To use:

1. pip install django-piston
2. Open /ToDo/settings.py and change the path to match your install
3. python manage.py runserver
3. Go to 127.0.0.1:8000
4. Add items to the list by typing them into the text box and clicking "Add Item"
5. Click on the checkmark to cross the item off the list
6. Click on the trashcan to delete an item (currently not functional)
7. After creating items and clicking on icons, go to http://127.0.0.1:8000/api/ to see a JSON dump of clicked images

Future improvements:
Recording link clicks
UI Improvements
Improving JSON layout
