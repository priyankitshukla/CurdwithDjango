from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='list_employee'),
    path('new', views.add, name='create_employee'),
    path('update/<int:id>/', views.update, name='update_employee'),
    path('delete/<int:id>/', views.delete, name='delete_employee'),
    path('detail', views.detail)
]

