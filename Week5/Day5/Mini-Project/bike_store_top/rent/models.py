from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.CharField(unique=True)
    phone_number = PhoneNumberField()
    address = models.CharField()
    city = models.CharField()
    country = models.CharField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class VehicleType(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class VehicleSize(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Address(models.Model):
    address = models.CharField()
    address2 = models.CharField()
    city = models.CharField()
    country = models.CharField()
    postal_code = models.IntegerField()


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.DO_NOTHING)
    date_created = models.DateField()
    real_cost = models.IntegerField()
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.DO_NOTHING)


class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)


class RentalRate(models.Model):
    daily_rate = models.IntegerField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)


class RentalStation(models.Model):
    station_name = models.CharField()
    capacity = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
