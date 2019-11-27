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


15- You may experience like Employee Object(1) in dropdown to get the proper name def __str__ method with model
 def __str__(self):
        return "%s HCL" % self.employee.first_name



############################ Create custom view #######################################


1- Go to views.py and add a function called index

from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.


def index(request):
    employee_list = Employee.objects.all()
    return render(request, 'employee.html', {'employee_list':employee_list})

2- Create a folder templates inside the employee package and create a html file called employee.html and add below content

<ul>
    {%  for employee in employee_list %}
    <li>{{ employee.first_name }}</li>
     {% endfor %}
</ul>


Tips-{% %} is statndard django tempate to write the code
     use {{ }} use double curly braces to render content dynamically

3- Create Operation

            1- go to urls.py and add below entry

            from django.urls import path
        from . import views


        urlpatterns = [
            path('', views.index, name='list_employee'),
            path('new', views.add, name='create_employee')
        ]

# name will get use while navigating using url look employee-form.html

    2- create a file called forms.py  inside the employee package and add below entry

        from django import forms
        from .models import Employee


        class ProductForm(forms.ModelForm):
                 class Meta:
                    model = Employee
                    fields = ['first_name', 'last_name', 'project', 'experience']

     3- now create html file for form named employee-form.html

                 <h1>Add/Update Employee</h1>
        <form method="post">
            {% csrf_token %}<!-- mandatory for all form django take cares of CSRF -->
            {{form}}
            <button type="submit">Save</button>
        </form>

        {% if employee %}
            <a href="{% url 'delete_employee' employee.id">Delete</a>
        {% endif %}

















