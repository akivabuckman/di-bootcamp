from .models import Project, Department, Task, Employee
from rest_framework import serializers

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields =('name', 'description', 'start_date', 'end_date', 'url')
        url = serializers.HyperlinkedIdentityField(view_name='project-detail')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'description', 'url')
        url = serializers.HyperlinkedIdentityField(view_name='department-detail')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='employee-detail')

    class Meta:
        model = Employee
        fields = ('name', 'email', 'phone_number', 'department', 'projects', 'url')
        url = serializers.HyperlinkedIdentityField(view_name='employee-detail')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'description', 'due_date', 'completed', 'project', 'url')
        url = serializers.HyperlinkedIdentityField(view_name='task-detail')