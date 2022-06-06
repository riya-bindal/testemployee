from django.test import TestCase
from ..models import Employees

class ModelsTestCase(TestCase):
    def setUp(self):
        Employees.objects.create(employee_name="Richa", department="IT",date_of_joining="2022-05-17")
        Employees.objects.create(employee_name="Satyam", department="CSE", date_of_joining="2022-05-17")

    def test_employees_created(self):
        
        emp1= Employees.objects.get(employee_name="Richa")
        emp2 = Employees.objects.get(employee_name="Satyam")
        self.assertEqual(emp1.employee_id , 4)
        self.assertEqual(emp2.employee_id, 5)