import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
import django

django.setup()
import datetime
import random
import rent.models
from faker import Faker
import psycopg2

fake = Faker(locale=['en_US', 'it_IT', 'fr_FR'])

CONNECTION = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='w5d5_mp')
CURSOR = CONNECTION.cursor()


def create_customers(number: int):
    for _ in range(number):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.msisdn()
        address = fake.address()
        city = fake.city()
        country = fake.country()
        customer = rent.models.Customer(first_name=first_name,
                                        last_name=last_name,
                                        email=email,
                                        phone_number=phone_number,
                                        address=address,
                                        city=city,
                                        country=country)

        customer.save()

    print(f"CREATED {number} Customers")


def create_vehicle_type(name: str):
    type = rent.models.VehicleType(name=name)
    type.save()


# create_vehicle_type('bicycle')
# create_vehicle_type('scooter')
# create_vehicle_type('jetpack')


def create_vehicle_sizes(sizes: list):
    for i in sizes:
        size = rent.models.VehicleSize(name=i)
        size.save()


# create_vehicle_sizes(['small', 'medium', 'large'])

def create_rental_rates(rate, type, size):
    type = rent.models.VehicleType.objects.filter(name=type)[0]
    size = rent.models.VehicleSize.objects.filter(name=size)[0]
    rate = rent.models.RentalRate(daily_rate=rate,
                                  vehicle_type=type,
                                  vehicle_size=size)
    rate.save()


# create_rental_rates(5,'scooter','small')
# create_rental_rates(15,'scooter','medium')
# create_rental_rates(25,'scooter','large')
# create_rental_rates(10, 'bicycle', 'small')
# create_rental_rates(20,'bicycle','medium')
# create_rental_rates(30,'bicycle','large')
# create_rental_rates(99,'jetpack','small')
# create_rental_rates(199,'jetpack','medium')
# create_rental_rates(299,'jetpack','large')

def get_random_date(start_date, end_date):
    all_dates = [start_date]
    while start_date != end_date:
        start_date += datetime.timedelta(days=1)
        all_dates.append(start_date)

    return random.choice(all_dates)


def create_vehicles(number: int):
    all_types = rent.models.VehicleType.objects.all()
    all_sizes = rent.models.VehicleSize.objects.all()
    start_date = datetime.date(1980, 1, 1)
    end_date = datetime.date(2022, 1, 1)
    for _ in range(number):
        vehicle_type = random.choice(all_types)
        date_created = get_random_date(start_date, end_date)
        real_cost = random.randint(1000, 2000)
        vehicle_size = random.choice(all_sizes)
        vehicle = rent.models.Vehicle(
            vehicle_type=vehicle_type,
            date_created=date_created,
            real_cost=real_cost,
            vehicle_size=vehicle_size
        )
        vehicle.save()


def create_rentals(number):
    for _ in range(number):
        print(_)
        all_vehicles = rent.models.Vehicle.objects.all()
        vehicle = random.choice(all_vehicles)
        earliest_rental_start = datetime.date(2023, 1, 1)
        today = datetime.date.today()
        customers = rent.models.Customer.objects.all()
        customer = random.choice(customers)

        # return db results of all vehicle's rentals
        # iterate through and make list of unavailable dates
        CURSOR.execute(f"SELECT rental_date, return_date FROM rent_rental WHERE vehicle_id = {vehicle.id}")
        rent_dates = CURSOR.fetchall()  # [(datetime.date(2023, 2, 1), datetime.date(2023, 2, 10)),
        # (datetime.date(2023, 3, 1), datetime.date(2023, 3, 10))]
        EPOCH = datetime.date(2000, 1, 1)
        rented_ints = []
        for i in rent_dates:
            if i[1] == None:
                rented_ints.append(((i[0] - EPOCH).days, (today - EPOCH).days))
            else:
                rented_ints.append(((i[0] - EPOCH).days, (i[1] - EPOCH).days))
        unavailable_days = []
        for i in rented_ints:
            for j in list(range(i[0], i[1])):
                unavailable_days.append(j)

        # create list of available days
        start_int = (earliest_rental_start - EPOCH).days
        today_int = (today - EPOCH).days
        available_days = [i for i in range(start_int, today_int) if i not in unavailable_days]
        try:
            rental_date_int = random.choice(available_days)
        except IndexError:
            pass
        else:
            try:
                available_till = min([i for i in unavailable_days if i > rental_date_int])
            except ValueError:
                available_till = today_int
            return_date_int = random.choice(list(range(rental_date_int, available_till + 1)))
            rental_date = EPOCH + datetime.timedelta(days=rental_date_int)
            return_date = None if random.randint(0, 7) == 1 else EPOCH + datetime.timedelta(days=return_date_int)
            rental = rent.models.Rental(
                rental_date=rental_date,
                return_date=return_date,
                customer=customer,
                vehicle=vehicle
            )
            rental.save()

# create_rentals(5000)

