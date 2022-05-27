from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Employees
from .serializers import EmployeeSerializer

# Create your views here.

class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

    # def list(self, request):
    #     queryset = Employees.objects.all()
    #     serializer = EmployeeSerializer(queryset, many=True)
    #     return Response(serializer.data)

class EmployeeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

    # def get(self, request):
    #     queryset = self.get_queryset()
    #     serializer = EmployeeSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # def put(self, request):
    #     queryset = self.get_queryset()
    #     serializer = EmployeeSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # def patch(self, request):
    #     queryset = self.get_queryset()
    #     serializer = EmployeeSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # def delete(self, request):
    #     queryset = self.get_queryset()
    #     serializer = EmployeeSerializer(queryset, many=True)
    #     return Response(serializer.data)
