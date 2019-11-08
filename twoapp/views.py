from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Student
from .serializer import StudentSerializer


class StudViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
