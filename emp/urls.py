from django.contrib import admin
from django.urls import path
from .views import views_emp

urlpatterns = [
    path('', views_emp.index, name='index'),
    path('myprofile', views_emp.myprofile, name='myprofile'),
    path('all_emp', views_emp.all_emp, name='all_emp'),
]