from django.db import models
import datetime

class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField(default=datetime.date.today)
    created_in_country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, related_name='created_in_country')
    available_in_countries = models.ManyToManyField(Country, related_name='available_in_countries')
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)

    def __str__(self) -> str:
        return self.title
