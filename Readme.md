```python
Install django using
    pip install django==2.1.5
To create base project setup-
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

6- Now make a reference of urls.py of employee package in base project urls.py which is employeecrud.django

       from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls'))
]

7- Create model - go to models.py in employee and add below class
          from django.db import models

# Create your models here.


class Employee(models.Model) :
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    project= models.CharField(max_length=20)
    experience= models.DecimalField(max_digits=9, decimal_places=2)

8- run below command to prepare migration, this will create a migration file in folder migrations
        python manage.py makemigrations

9- to create actual database tables run below command

        python manage.py migrate

10- to view sqlite database download database browser from # Download sqllite browser https://sqlitebrowser.org/dl/ and open file db.sqlite2

11- Now to login with admin use url http://localhost:8000/admin to access the admin module we need to create a super user

        command- python manage.py createsuperuser

12- Now register employee Model to admin
        1- go to employee package
        2- open file admin.py
        3- use below snippet

from django.contrib import admin
from .models import Employee

# Register your models here.

admin.site.register(Employee)


13- Now to list attributes in table add below code using modelAdmin in admin.py under employee package.

from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'project', 'experience')

admin.site.register(Employee,EmployeeAdmin)


14-  Exercise - Introduce a new model for department.



