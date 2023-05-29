from django.db import models

class Family(models.Model):
    name = models.CharField()


class Animal(models.Model):
    name = models.CharField()
    legs = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    speed = models.IntegerField()
    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)