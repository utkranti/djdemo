from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Employee
from .serializer import EmployeeSerializer

class EmpViewset(ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

