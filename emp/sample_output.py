from collections import OrderedDict

post_input_data = {
    "employee_name": "Riya",
    "department":"IT",
    "date_of_joining": "2022-05-17"
}

get_employee_sample_output = [OrderedDict([('employee_id', 1), ('employee_name', 'John'), ('department', 'IT'), ('date_of_joining', '2022-05-20')]), OrderedDict([('employee_id', 2), ('employee_name', 'VK'), ('department', 'Admin'), ('date_of_joining', '2022-05-21')])]

# Employees.objects.all().values()
# <QuerySet [{'employee_id': 50, 'user_id': None, 'department': 'IT', 'date_of_joining': datetime.date(2022, 5, 17)}, {'employee_id': 52, 'user_id': None, 'department': 'IT', 'date_of_joining': datetime.date(2022, 5, 17)}, {'employee_id': 53, 'user_id': None, 'department': 'IT', 'date_of_joining': datetime.date(2022, 5, 17)}, {'employee_id': 54, 'user_id': None, 'department': 'IT', 'date_of_joining': datetime.date(2022, 5, 17)}, {'employee_id': 4, 'user_id': None, 'department': 'IT', 'date_of_joining': datetime.date(2022, 5, 17)}, {'employee_id': 64, 'user_id': None, 'department': 'Inventory', 'date_of_joining': datetime.date(2022, 5, 23)}, {'employee_id': 65, 'user_id': None, 'department': 'Inventory', 'date_of_joining': datetime.date(2019, 9, 19)}]>