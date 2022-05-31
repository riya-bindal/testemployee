"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# import rest_framework
from emp.views import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emp.urls')),
    path("accounts/", include("django.contrib.auth.urls")),

    
    path('emp_list/', views.EmployeeListView.as_view()),
    path('emp_create/', views.EmployeeCreateView.as_view()),
    path('emp_change/<int:pk>/', views.EmployeeChangeView.as_view()),
    path('emp_read/<int:pk>/', views.EmployeeRetrieveView.as_view()),
    path('emp_delete/<int:pk>/', views.EmployeeDeleteView.as_view()),
    # path('api-auth/',include('rest_framework.urls')),

]