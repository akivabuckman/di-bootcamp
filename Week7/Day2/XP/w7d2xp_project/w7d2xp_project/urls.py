from django.contrib import admin
from django.urls import path, include
from w7d2xp_app.views import DepartmentListAPIView, DepartmentCreateAPIView, EmployeeListAPIView, EmployeeCreateAPIView, ProjectRetrieveAPIView, ProjectUpdateAPIView, ProjectDestroyAPIView, TaskRetrieveAPIView, TaskUpdateAPIView, TaskDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('departments/', DepartmentListAPIView.as_view(), name='department-list'),
    path('create-department/', DepartmentCreateAPIView.as_view(), name='create-department'),
    path('employees/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('create-employee/', EmployeeCreateAPIView.as_view(), name='create-employee'),
    path('projects/', ProjectRetrieveAPIView.as_view(), name='project-list'),
    path('update-project/', ProjectUpdateAPIView.as_view(), name='update-project'),
    path('destroy-object/', ProjectDestroyAPIView.as_view(), name='destroy-project'),
    path('tasks/', TaskRetrieveAPIView.as_view(), name='task-list'),
    path('update-task/', TaskUpdateAPIView.as_view(), name='update-task'),
    path('destroy-task/', TaskDestroyAPIView.as_view(), name='destroy-task'),
]
