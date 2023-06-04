import os
from .forms import RentalForm
from .models import Rental
from django.shortcuts import render

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')

import datetime
import random
from faker import Faker
import psycopg2


def add_rental(request):
    # if request.method == 'POST':
    #     form_filled = TodoForm(request.POST)
    #     if form_filled.is_valid():
    #         form_filled.save()
    #     else:
    #         print(form_filled.errors)
    # # GET
    # todo_form = TodoForm()
    # context = {'form': todo_form}
    # return render(request, 'add_todo.html', context)

    if request.method == 'POST':
        data = request.POST
        filled_form = RentalForm(data)
        if filled_form.is_valid():
            print(data)
            # filled_form.save()
        else:
            print(filled_form.errors)

    rental_form = RentalForm()
    context = {'form': rental_form}
    return render(request, 'add_rental.html', context)

