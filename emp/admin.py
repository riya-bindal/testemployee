from django.contrib import admin

from emp.models import Departments, Employees, Role

# Register your models here.
admin.site.register(Employees)
admin.site.register(Departments)
admin.site.register(Role)