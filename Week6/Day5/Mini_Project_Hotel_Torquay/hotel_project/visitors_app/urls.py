from django.contrib import admin
from django.urls import path, include
from .views import BookingSuccess, CreateBooking, visitor_home_page, RegisterView, CustomLoginView, Booking
from django.contrib.auth import views

urlpatterns = [
    path('info-page/', visitor_home_page, name='info-page'),
    path('visitor-login/', CustomLoginView.as_view(template_name='visitor_login.html'), name='visitor-login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('vacancies/', Booking.as_view(), name='vacancies'),
    path('book/<str:date>', CreateBooking.as_view(), name='create_booking'),
    path('booking_success/', BookingSuccess.as_view(), name='booking_success')
]