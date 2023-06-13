from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_employee')
    projects = models.ManyToManyField(Project, related_name='project_employee')


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_task')

