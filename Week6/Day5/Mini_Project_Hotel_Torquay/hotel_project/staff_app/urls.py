from django.contrib import admin
from django.urls import path, include
from .views import BookingListView, BookingDetailView, create_booking, DeleteBooking, update_booking

urlpatterns = [
    path('booking_list/', BookingListView.as_view(), name='booking_list'),
    path('booking_detail/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('new_booking/', create_booking, name='new_booking'),
    path('delete_booking_confirm/<int:pk>', DeleteBooking.as_view(), name='delete_booking_confirm'),
    path('update_booking/<int:booking_id>', update_booking, name='update_booking')
]
