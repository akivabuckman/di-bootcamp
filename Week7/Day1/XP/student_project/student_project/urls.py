from django.contrib import admin
from django.urls import path, include
from student_app.views import StudentListView, StudentDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/students/', StudentListView.as_view(), name='students'),
    path('api/students/<pk>', StudentDetailView.as_view(), name='student')
]
