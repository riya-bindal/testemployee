from django.db import models
from employee.settings import AUTH_USER_MODEL


# Create your models here
class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=500)

class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    user=models.OneToOneField(AUTH_USER_MODEL, on_delete = models.CASCADE, null=True)
    department = models.CharField(max_length=500)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.user.username

