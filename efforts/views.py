from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from efforts.models import Customer, Project, Effort
from efforts.serializers import CustomerSerializer, ProjectSerializer, EffortSerializer
# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class EffortViewSet(viewsets.ModelViewSet):
    queryset = Effort.objects.all()
    serializer_class = EffortSerializer
    permissions = [permissions.IsAdminUser]
