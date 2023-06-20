from django.contrib import admin
from django.urls import path, include
from .views import BookingListView, BookingDetailView

urlpatterns = [
    path('booking_list/', BookingListView.as_view(), name='booking_list'),
    path('booking_detail/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
]
