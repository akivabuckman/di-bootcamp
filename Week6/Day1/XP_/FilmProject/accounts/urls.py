from django.urls import path
from django.contrib.auth import views
from .views import Signup, ProfileView

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', Signup.as_view(template_name='signup.html'), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]