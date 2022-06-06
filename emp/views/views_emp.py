
from django.shortcuts import render, HttpResponse
from ..models import Employees, Role, Departments
from utilities.models import User
from datetime import datetime
from django.db.models import Q

from django.contrib.auth.decorators import login_required, user_passes_test

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

@user_passes_test(lambda user: user.is_staff)
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept_name = (request.POST['dept'])
        role_name = (request.POST['role'])

        # new_user=User.objects.create(username=first_name+last_name)
        dept=Departments.objects.get_or_create(department_name=dept_name)[0]
        role=Role.objects.get_or_create(name=role_name)[0]
        print(dept)
        new_emp = Employees(user=User(username=first_name+last_name), salary=salary, phone_number=phone, department = dept, role = role, date_of_joining = datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")

# text = f"""
#         Some attributes of the HttpRequest object:

#         scheme: {request.scheme}
#         path:   {request.path}
#         method: {request.method}
#         GET:    {request.GET}
#         user:   {request.user}
#         username:     {request.user.username}
#         is_anonymous: {request.user.is_anonymous}
#         is_staff:     {request.user.is_staff}
#         is_superuser: {request.user.is_superuser}
#         is_active:    {request.user.is_active}"""
#print(text) #<!-- {% extends 'base.html' %} #{% block content %} #{% endblock %}

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employees.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employees.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employees.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')