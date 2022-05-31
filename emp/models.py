from django.db import models
from employee.settings import AUTH_USER_MODEL


# Create your models here
class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name

class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    user=models.OneToOneField(AUTH_USER_MODEL, on_delete = models.CASCADE)
    # picture = models.FileField(blank=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    date_of_joining = models.DateField()
    salary=models.DecimalField(max_digits=7, decimal_places=2)
    phone_number = models.CharField(max_length=17, blank=True)

    def __str__(self):
        return self.user.username

