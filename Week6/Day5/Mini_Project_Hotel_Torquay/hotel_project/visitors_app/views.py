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
import random

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


class CreateBooking(CreateView, LoginRequiredMixin):
    model = Booking
    form_class = BookingForm
    template_name = 'create_booking.html'
    login_url = reverse_lazy('visitor_login')
    success_url = reverse_lazy('booking_success')

    def dates_between(self, start_date, end_date):
        delta = end_date - start_date
        dates = [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
        return dates

    def get_initial(self):
        given_string = self.kwargs['date']
        self.start_date = datetime.datetime.strptime(given_string, '%Y%m%d').date()
        self.end_date = self.start_date + datetime.timedelta(1)
        return {
            'user': self.request.user,
            'user_id': self.request.user,
            'start_date': self.start_date,
            'end_date': self.end_date
        }

    def form_valid(self, form):
        form.instance.duration = (form.instance.end_date - form.instance.start_date).days
        all_dates = self.dates_between(self.start_date, self.end_date)
        big_enough_rooms = []
        k = 0
        while len(big_enough_rooms) == 0:
            big_enough_rooms = Room.objects.filter(capacity=form.instance.person_count + k)
            k += 1
        for room in big_enough_rooms:
            if all(day in room.dates for day in all_dates):
                form.instance.save()
                form.instance.room.set([room])

                break
        CURSOR.execute(f"SELECT room_id FROM visitors_app_booking_room WHERE booking_id = {form.instance.id}")
        room_id = CURSOR.fetchone()[0]
        daily_rate = Room.objects.filter(id=room_id)[0].daily_rate
        form.instance.price = daily_rate * form.instance.duration
        form.instance.save()
        form.instance.save_m2m()
        return super().form_valid(form)



class BookingSuccess(DetailView):
    pass
#     model = Booking
#     template_name = 'booking_success.html'
#     context_object_name = 'details'
