from django.contrib import admin
from django.urls import path
from polls.views import posts, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('whatever_i_want/', posts),
    path('profile_user/', profile),
]
