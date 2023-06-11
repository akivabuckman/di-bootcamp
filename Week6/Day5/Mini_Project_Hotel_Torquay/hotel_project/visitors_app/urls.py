from django.contrib import admin
from django.urls import path, include
from .views import visitor_home_page, RegisterView, CustomLoginView
from django.contrib.auth import views

urlpatterns = [
    path('info-page/', visitor_home_page, name='info-page'),
    path('visitor-login/', CustomLoginView.as_view(template_name='visitor_login.html'), name='visitor-login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]