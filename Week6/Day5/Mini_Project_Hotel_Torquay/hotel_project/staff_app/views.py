from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from visitors_app.models import Booking, Room
import psycopg2

CONNECTION = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='w6d5mp6')
CURSOR = CONNECTION.cursor()


class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'
    redirect_field_name = reverse_lazy('login')

    def get_queryset(self):
        objects = Booking.objects.all().order_by('id')
        return objects


class BookingDetailView(DetailView):
    model = Booking
    template_name = 'booking_detail.html'
    context_object_name = 'details'
    redirect_field_name = reverse_lazy('login')

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs['pk']
        selected = queryset.filter(id=pk)
        return selected

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        CURSOR.execute(f"SELECT room_id FROM visitors_app_booking_room WHERE booking_id = {context['object'].id}")
        room_id = CURSOR.fetchone()[0]
        room_object = Room.objects.filter(id=room_id)[0]
        context['room_number'] = room_object.room_number
        print(context)
        return context
