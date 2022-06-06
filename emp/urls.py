from django.contrib import admin
from django.urls import path
from .views import views_emp

urlpatterns = [
    path('', views_emp.index, name='index'),
    path('myprofile', views_emp.myprofile, name='myprofile'),
    path('all_emp', views_emp.all_emp, name='all_emp'),
    path('add_emp', views_emp.add_emp, name='add_emp'),
    path('remove_emp', views_emp.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>', views_emp.remove_emp, name='remove_emp'),
    path('filter_emp', views_emp.filter_emp, name='filter_emp'),
]

