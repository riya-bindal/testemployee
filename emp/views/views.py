from django.shortcuts import render

from rest_framework.generics import GenericAPIView,ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from ..models import Employees
from ..serializers import EmployeeSerializer

# Create your views here.

class EmployeeCreateView(CreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes=[IsAdminUser]

class EmployeeListView(ListAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes=[IsAuthenticated]

class EmployeeChangeView(UpdateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes=[IsAdminUser]

class EmployeeRetrieveView(RetrieveAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes=[IsAuthenticated]

class EmployeeDeleteView(DestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes=[IsAdminUser]