from django.contrib import admin
from django.urls import path
from ..films.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', HomePageView, name='homepage')
]
