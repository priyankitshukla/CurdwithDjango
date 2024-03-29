
# CRUD with Django and sqlite

###### Install django using
```
        pip install django==2.1.5 or run pip install -r reqirements.txt
```

######  Setup base project using below command.
```
        django-admin startproject employeecrud .
```
######  Now create a employee module/app using below command
```
        python manage.py startapp employee
```
###### Now to register employee module, add an entry in settings.py in base project for INSTALLED APP SECTION get the app name from the module apps.py.
```python
        INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'employee.apps.EmployeeConfig'
    ]
```

## Lets create a endpoint to print Hello World

1.Navigate to employee package.
2.Go to views.py
3.Add import for HttpResponse
```python
        from django.http import HttpResponse
```
4.define index method like below.
```python
		def index(request):
             return HttpResponse("Hello world")
```
5.Now create a file name urls.py in employee package.make entry exactly like below,

        1. add entry from django.url import path.
        2. import view using
```python
from . import views
from django.urls import path
from . import views


urlpatterns=[
    path('',views.index)
]
```
6. Now make a reference of urls.py of employee package in base project urls.py which is employeecrud.django
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls'))
]
```

# Introduce Model/Tables
###### Create model - go to models.py in employee and add below class
```python
from django.db import models
class Employee(models.Model) :
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    project= models.CharField(max_length=20)
    experience= models.DecimalField(max_digits=9, decimal_places=2)
```
###### run below command to prepare migration, this will create a migration file in folder migrations
```
                 python manage.py makemigrations
```
###### create actual database tables run below command
```
                 python manage.py migrate
```
###### To view sqlite database download database browser from # [Download sqlite browser](https://sqlitebrowser.org/dl/) and open file db.sqlite2

###### Now to login with admin use url http://localhost:8000/admin to access the admin module we need to create a super user
```command
                 python manage.py createsuperuser
```
###### Now register employee Model to admin
        1. Go to employee package
        2. Open file admin.py
        3. Use below snippet
```python
from django.contrib import admin
from .models import Employee

admin.site.register(Employee)

```
###### Now to list attributes in table add below code using modelAdmin in admin.py under employee package.
```python
from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'project', 'experience')

admin.site.register(Employee,EmployeeAdmin)
```

## Exercise - Introduce a new model for department.

###### Now login t

###### You may experience like Employee Object(1) in dropdown to get the proper name def __str__ method with model
```python
                    def __str__(self):
                            return "%s HCL" % self.employee.first_name
```

# Create custom view

## Read Operation

1. Go to views.py and add a function called index
```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.


def index(request):
    employee_list = Employee.objects.all()
    return render(request, 'employee.html', {'employee_list':employee_list})
```
2. Create a folder templates inside the employee package and create a html file called employee.html and add below content
```html
<ul>
    {%  for employee in employee_list %}
    <li>{{ employee.first_name }}</li>
     {% endfor %}
</ul>
```

###### Tips-{% %} is standard django template to write the code, use {{ }} use double curly braces to render content dynamically

## Create Operation

1. Go to urls.py and add below entry
```python
from django.urls import path
from . import views


urlpatterns = [
       path('', views.index, name='list_employee'),
       path('new', views.add, name='create_employee')
      ]
```
###### name attribute inside the path will get use while navigating using url look employee-form.html

2. Create a file called forms.py  inside the employee package and add below entry
```python
        from django import forms
        from .models import Employee


        class ProductForm(forms.ModelForm):
                 class Meta:
                    model = Employee
                    fields = ['first_name', 'last_name', 'project', 'experience']
```
3. now create html file for form named employee-form.html
```html
      <h1>Add/Update Employee</h1>
        <form method="post">
            {% csrf_token %}<!-- mandatory for all form django take cares of CSRF -->
            {{form}}
            <button type="submit">Save</button>
        </form>

        {% if employee %}
            <a href="{% url 'delete_employee' employee.id">Delete</a>
        {% endif %}

```
## Update operation
1. Add a new def for update in views.py
```python
        def update(request, id):
            employee = Employee.objects.get(id=id)
            form = EmployeeForm(request.POST or None, instance= employee)

        if form.is_valid():
            form.save()
            return redirect('list_employee')

        return render(request, 'employee-form.html', {'form': form, 'employee': employee})

```
2. make entry in urls.py this time add url like update/<int:id> to get id from the url

3. update the employee.html make first name surrounded with a hyperlink
```html
            <a href="{% url 'update_employee' employee.id %}">
                      <li>{{ employee.first_name }}</li>
               </a>
```

## Delete Operation
1.           Introduce a method in views.py
```python
def delete(request, id):
      employee = Employee.objects.get(id=id)

if request.method == 'POST':
    employee.delete()
    return redirect('list_employee')

return render(request, 'emp-delete-confirm.html', {'employee': employee})
```


2. add entry in urls.py
```python
            path('delete/<int:id>/', views.delete, name='delete_employee')
```

3. add footer in employee-form.html
```python
                         {% if employee %}
                               <a href="{% url 'delete_employee' employee.id%}">Delete</a>
                         {% endif %}
```



##  Integrating Bootstrap

######Install bootstrap

1. create a file name base.html

2. [Download Bootstrap Template](https://getbootstrap.com/docs/4.3/getting-started/introduction/) and copy the code for base template

3. Inside body section create a django template tag with block and name it as content like

             {%  block content %}
                {%  endblock %}

Step 4- import base file in employee.html



# References  -------------------------


1. [Customize forms](https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html)
2. [I18](http://www.marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones)
3. [Consume rest api](https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html)


# Create a virtual env
```
python -m venv venv
then go to /bin
and execture activate
```


Then
```
pip install -r requirements.txt
```

Happy learning
[Priyankit](https://www.linkedin.com/in/priyankit-shukla-aa28a821/)




















