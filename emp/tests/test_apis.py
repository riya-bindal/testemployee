from django.test import TestCase
from django.test import Client
from ..models import Employees

from ..sample_output import get_employee_sample_output, post_input_data
import json



# Create your tests here.
class TestAPI(TestCase):
    c = Client()

    def setUp(self):
        response = self.c.post('/emp/', {"employee_name": "John","department":"IT","date_of_joining": "2022-05-20"})
        response = self.c.post('/emp/', {"employee_name": "VK","department":"Admin","date_of_joining": "2022-05-21"})

    def TestPost(self):
        response = self.c.post('/emp/', post_input_data)
        self.post_data_pk = response.data['employee_id']
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['employee_name'],post_input_data['employee_name'])
    
    def TestList(self):
        response = self.c.get('/emp/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, get_employee_sample_output)


    def TestGet(self):
        response = self.c.get('/emp/{}/'.format(self.post_data_pk))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['employee_id'], Employees.objects.get(employee_id=self.post_data_pk).employee_id)
        

    def TestPatch(self):
        response = self.c.patch('/emp/{}/'.format(self.post_data_pk), data=json.dumps({"employee_name": "Rishabh"}), content_type='application/json')
        self.assertEquals(response.status_code, 200)

        emp_obj=Employees.objects.get(employee_id=self.post_data_pk)
        self.assertEquals(response.data['employee_id'], emp_obj.employee_id)
        self.assertEquals("Rishabh", emp_obj.employee_name)

    def TestPut(self):
        response = self.c.put('/emp/{}/'.format(self.post_data_pk), data=json.dumps({"employee_name": "xyz","department":"IT","date_of_joining": "2022-05-17"}), content_type='application/json')
        self.assertEquals(response.status_code, 200)

        emp_obj=Employees.objects.get(employee_id=self.post_data_pk)
        self.assertEquals(response.data['employee_id'], emp_obj.employee_id)
        self.assertEquals("xyz", emp_obj.employee_name)

    def TestDelete(self):
        response = self.c.delete('/emp/{}/'.format(self.post_data_pk))
        self.assertEquals(response.status_code, 204)

    def test_sequence(self):
        self.TestPost()
        self.TestGet()
        self.TestPut()
        self.TestPatch()
        self.TestDelete()
        self.TestList()

