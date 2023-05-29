from django.contrib import admin
from django.urls import path
from polls.views import posts, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts, name='posts'),
    path('profile/', profile)
]
