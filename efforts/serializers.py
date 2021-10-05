from rest_framework import serializers
from efforts.models import Customer, Product, Project, Team, Employee, Effort


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'name', 'projects']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'projects']


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name', 'customer', 'product']


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'name']


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'name']


class EffortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Effort
        fields = ['id', 'employee', 'project', 'interval']
