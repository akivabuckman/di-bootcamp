from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from visitors_app.models import Booking, Room
import psycopg2
import datetime
from .forms import BookingForm
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin





CONNECTION = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='w6d5mp6')
CURSOR = CONNECTION.cursor()


class BookingListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'
    redirect_field_name = reverse_lazy('login')

    def get_queryset(self):
        objects = Booking.objects.all().order_by('id')
        return objects

    def test_func(self):
        return self.request.user.is_staff



class BookingDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    def test_func(self):
        return self.request.user.is_staff

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

def dates_between(start_date, end_date):
    delta = end_date - start_date
    dates = [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
    return dates

@staff_member_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            all_dates = dates_between(start_date, end_date)
            form.duration = len(all_dates)
            big_enough_rooms = []
            k = 0
            while len(big_enough_rooms) == 0:
                big_enough_rooms = Room.objects.filter(capacity=form.cleaned_data['person_count'] + k)
                k += 1
            for room in big_enough_rooms:
                if all(day in room.dates for day in all_dates):
                    booking = form.save(commit=False)
                    booking.duration = form.duration
                    booking.price = Room.objects.filter(id=room.id)[0].daily_rate * form.duration
                    booking.save()
                    booking.room.add(room)
                    CURSOR.execute(f"DELETE FROM visitors_app_booking_room WHERE booking_id={booking.id}")
                    CURSOR.execute(
                        f"INSERT INTO visitors_app_booking_room(booking_id, room_id) VALUES ({booking.id}, {room.id})")
                    pre_booking_dates = room.dates
                    for day in all_dates:
                        pre_booking_dates.remove(day)

                    room.dates = ArrayField(
                        base_field=ArrayField(base_field=models.DateField()),
                        default=list,
                    ).to_python(pre_booking_dates)

                    room.save()
                    # CURSOR.execute(f"UPDATE visitors_app_room SET dates={pre_booking_dates} WHERE id={room.id}")
                    return render(request, 'booking_success.html', {'price': booking.price,
                                                                    'start': booking.start_date,
                                                                    'end': booking.end_date,
                                                                    'duration': booking.duration,
                                                                    'count': room.capacity,
                                                                    'room': room.room_number})
    else:
        form = BookingForm(initial={
            'user': request.user,
            'user_id': request.user,
            'start_date': datetime.date(2023,7,1),
            'end_date': datetime.date(2023,7,2)
        })

    return render(request, 'staff_create_booking.html', {'form': form})

class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = 'delete_booking_confirm.html'
    success_url = reverse_lazy('booking_list')
    context_object_name = 'details'

    def test_func(self):
        return self.request.user.is_staff


@staff_member_required

def update_booking(request, booking_id):
    if request.method == "GET":
        booking_id = booking_id
        current_obj = Booking.objects.filter(id=booking_id)[0]
        print(current_obj.user_id)
        form = BookingForm(initial={
            'person_count': current_obj.person_count,
            'start_date': current_obj.start_date,
            'end_date': current_obj.end_date,
        })

        return render(request, 'update_booking.html', {'form': form, 'booking_id': booking_id})

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            current_obj = Booking.objects.filter(id=booking_id)[0]
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            new_dates = dates_between(start_date, end_date)
            old_dates = dates_between(current_obj.start_date, current_obj.end_date)
            form.duration = len(new_dates)
            big_enough_rooms = []
            k = 0
            while len(big_enough_rooms) == 0:
                big_enough_rooms = Room.objects.filter(capacity=form.cleaned_data['person_count'] + k)
                k += 1
            for room in big_enough_rooms:
                if all(day in room.dates for day in new_dates):
                    booking = form.save(commit=False)
                    booking.id = booking_id
                    booking.duration = form.duration
                    booking.price = Room.objects.filter(id=room.id)[0].daily_rate * form.duration
                    booking.save()
                    booking.room.add(room)
                    CURSOR.execute(f"DELETE FROM visitors_app_booking_room WHERE booking_id={booking_id} AND room_id != {room.id}")
                    CONNECTION.commit()
                    pre_booking_dates = room.dates
                    for day in new_dates:
                        pre_booking_dates.remove(day)
                    for day in old_dates:
                        pre_booking_dates.append(day)
                    room.dates = ArrayField(
                        base_field=ArrayField(base_field=models.DateField()),
                        default=list,
                    ).to_python(pre_booking_dates)

                    room.save()
                    return render(request, 'booking_success.html', {'price': booking.price,
                                                                    'start': booking.start_date,
                                                                    'end': booking.end_date,
                                                                    'duration': booking.duration,
                                                                    'count': room.capacity,
                                                                    'room': room.room_number})