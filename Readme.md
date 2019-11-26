```python
django-admin startproject pythonwebshop .
python manage.py startapp employee
Add an entry in settings.py in base project for INSTLLED APP SECTION get the app name from the module apps.py.
Now to create first endpoint

1- Navigate to employee package.
2- Go to views.py
3- add import for
		-from django.http import HttpResponse
4- define index method like below.

		def index(request):
    return HttpResponse("Hello world")
5- Now create a file name urls.py in employee package.make entry exactly like below,

1- add entry from django.url import path.
2- import view using from . import views

		from django.urls import path
from . import views


urlpatterns=[
    path('',views.index)
]