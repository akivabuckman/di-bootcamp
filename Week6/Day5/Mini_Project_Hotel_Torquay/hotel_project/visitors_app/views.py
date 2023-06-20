from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from .models import Booking, Room
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
import datetime
import psycopg2
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres import forms as pg_forms
from datetime import date
from django.db import models

CONNECTION = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='w6d5mp6')
CURSOR = CONNECTION.cursor()


def visitor_home_page(request):
    context = {
        'user': request.user
    }
    return render(request, 'info_page.html', context)


class RegisterView(CreateView):
    form_class = RegisterForm
    model = User
    template_name = 'visitor-register.html'
    success_url = reverse_lazy('visitor-login')


class CustomLoginView(LoginView):
    success_url = reverse_lazy('info-page')


class Booking(ListView):
    model = Booking
    template_name = 'vacancies.html'
    context_object_name = 'vacancies'
    redirect_field_name = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        all_rooms = list(Room.objects.all())
        all_dates = set()
        for room in all_rooms:
            for day in room.dates:
                all_dates.add(day)
        dates_list = []
        for i in all_dates:
            dates_list.append([i, i.strftime("%Y%m%d")])
        dates_list.sort()
        context['available_dates'] = dates_list
        return context


# class CreateBooking(CreateView, LoginRequiredMixin):
#     model = Booking
#     form_class = BookingForm
#     template_name = 'create_booking.html'
#     login_url = reverse_lazy('visitor_login')
#     success_url = reverse_lazy('booking_success')
#
#     def dates_between(self, start_date, end_date):
#         delta = end_date - start_date
#         dates = [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
#         return dates
#
#     def get_initial(self):
#         given_string = self.kwargs['date']
#         self.start_date = datetime.datetime.strptime(given_string, '%Y%m%d').date()
#         self.end_date = self.start_date + datetime.timedelta(1)
#         return {
#             'user': self.request.user,
#             'user_id': self.request.user,
#             'start_date': self.start_date,
#             'end_date': self.end_date
#         }
#
#     def form_valid(self, form):
#         form.instance.duration = (form.instance.end_date - form.instance.start_date).days
#         all_dates = self.dates_between(self.start_date, self.end_date)
#         big_enough_rooms = []
#         k = 0
#         while len(big_enough_rooms) == 0:
#             big_enough_rooms = Room.objects.filter(capacity=form.instance.person_count + k)
#             k += 1
#         for room in big_enough_rooms:
#             if all(day in room.dates for day in all_dates):
#                 form.instance.save()
#                 form.instance.room.set([room])
#
#                 break
#         CURSOR.execute(f"SELECT room_id FROM visitors_app_booking_room WHERE booking_id = {form.instance.id}")
#         room_id = CURSOR.fetchone()[0]
#         daily_rate = Room.objects.filter(id=room_id)[0].daily_rate
#         form.instance.price = daily_rate * form.instance.duration
#         form.instance.save()
#         form.instance.save_m2m()
#         return super().form_valid(form)


def dates_between(start_date, end_date):
    delta = end_date - start_date
    dates = [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
    return dates


def create_booking(request, date):
    if request.method == "GET":
        given_string = date
        start_date = datetime.datetime.strptime(given_string, '%Y%m%d').date()
        end_date = start_date + datetime.timedelta(1)

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
            'start_date': start_date,
            'end_date': end_date
        })

    return render(request, 'create_booking.html', {'form': form})


class BookingSuccess(DetailView):
    pass
#     model = Booking
#     template_name = 'booking_success.html'
#     context_object_name = 'details'
