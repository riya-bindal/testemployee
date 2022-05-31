
from django.shortcuts import render, HttpResponse
from ..models import Employees, Role, Departments
from datetime import datetime
from django.db.models import Q

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def all_emp(request):
    emps = Employees.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)

@login_required
def myprofile(request):
    emp=Employees.objects.get(user=request.user)
    context={'emp':emp}
    print(context)
    return render(request, 'myprofile.html', context)