import os
from .forms import RentalForm, CustomerForm, VehicleForm
from .models import Rental, Customer, Vehicle
from django.shortcuts import render

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')

import datetime
import random
from faker import Faker
import psycopg2


def add_rental(request):
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

def view_rental(request, pk):
    all_rentals = Rental.objects.all()
    context = {}
    for i in all_rentals:
        if i.id == pk:
            context['hit'] = i
    return render(request, 'view_rental.html', context)
def view_rentals(request):
    all_rentals = Rental.objects.all()
    unreturned = [i for i in all_rentals if i.return_date == None]
    returned = [i for i in all_rentals if i not in unreturned]
    unreturned_sorted = sorted(unreturned, key=lambda x: x.rental_date, reverse=True)
    returned_sorted = sorted(returned, key=lambda x: x.rental_date, reverse=True)
    rental_list = unreturned_sorted + returned_sorted
    context = {'instances': rental_list}
    return render(request, 'view_rentals.html', context)

def view_customer(request, pk):
    all_customers = Customer.objects.all()
    context = {}
    for i in all_customers:
        if i.id == pk:
            context['hit'] = i
    return render(request, 'view_customer.html', context)

def view_customers(request):
    all_cusomters = Customer.objects.all()
    customers_sorted = sorted(all_cusomters, key=lambda x: x.last_name)
    context = {'instances': customers_sorted}
    return render(request, 'view_customers.html', context)

def add_customer(request):
    if request.method == 'POST':
        data = request.POST
        filled_form = CustomerForm(data)
        if filled_form.is_valid():
            filled_form.save()
        else:
            print(filled_form.errors)

    customer_form = CustomerForm()
    context = {'form': customer_form}
    return render(request, 'add_customer.html', context)

def view_vehicles(request):
    all_vehicles = Vehicle.objects.all()
    vehicles_sorted = sorted(all_vehicles, key=lambda x: x.vehicle_type_id)
    context = {'instances': vehicles_sorted}
    return render(request, 'view_vehicles.html', context)

def view_vehicle(request, pk):
    all_vehicles = Vehicle.objects.all()
    context = {}
    for i in all_vehicles:
        if i.id == pk:
            context['hit'] = i
    return render(request, 'view_vehicle.html', context)


def add_vehicle(request):
    if request.method == 'POST':
        data = request.POST
        filled_form = VehicleForm(data)
        if filled_form.is_valid():
            filled_form.save()
        else:
            print(filled_form.errors)

    vehicle_form = VehicleForm()
    context = {'form': vehicle_form}
    return render(request, 'add_rental.html', context)