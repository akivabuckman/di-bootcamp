from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    name = models.CharField()
    email = models.CharField(unique=True)
    phone_number = PhoneNumberField()
    address = models.CharField(blank=True)
    