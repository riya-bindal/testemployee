from django.test import TestCase
import unittest
from django.test import Client

from ..sample_output import get_employee_sample_output, post_input_data
import json



# Create your tests here.
class TestAPI(unittest.TestCase):
    c = Client()

    def TestPost(self):
        print("test_post")
        response = self.c.post('/emp/', post_input_data)
        self.post_data_pk = response.data['employee_id']
        self.assertEquals(response.status_code, 201)

    def TestGet(self):
        response = self.c.get('/emp/')
        # self.assertEquals(response.data, get_employee_sample_output)
        self.assertEquals(response.status_code, 200)

    def TestPatch(self):
        response = self.c.patch('/emp/{}/'.format(self.post_data_pk), data=json.dumps({"employee_name": "Rishabh"}), content_type='application/json')
        self.assertEquals(response.status_code, 200)

    def TestPut(self):
        response = self.c.put('/emp/{}/'.format(self.post_data_pk), data=json.dumps({"employee_name": "xyz","department":"IT","date_of_joining": "2022-05-17"}), content_type='application/json')
        self.assertEquals(response.status_code, 200)

    def TestDelete(self):
        print("test_delete")
        response = self.c.delete('/emp/{}/'.format(self.post_data_pk))
        self.assertEquals(response.status_code, 204)

    def test_sequence(self):
        self.TestPost()
        self.TestGet()
        self.TestPut()
        self.TestPatch()
        self.TestDelete()

