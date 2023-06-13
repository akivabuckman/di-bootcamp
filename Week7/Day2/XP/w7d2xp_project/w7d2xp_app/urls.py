from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DepartmentViewSet, EmployeeViewSet

router = DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('employees', EmployeeViewSet)

urlpatterns = [
   path('', include(router.urls))
]