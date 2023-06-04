from django.db import models
import datetime

class Country(models.Model):
    name = models.CharField()

class Category(models.Model):
    name = models.CharField()


class Director(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()


class Film(models.Model):
    title = models.CharField()
    release_date = models.DateField(default=datetime.date.today())
    created_in_country = models.ForeignKey(Country)
    available_in_countries = models.ManyToManyField(Country)
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)
