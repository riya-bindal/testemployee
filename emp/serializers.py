from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import Employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"