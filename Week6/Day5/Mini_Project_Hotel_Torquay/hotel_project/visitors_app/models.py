from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models import F
from django.contrib.postgres.fields import ArrayField


class VisitorUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='visitor_user')
    def __str__(self):
        return self.user.username

class Booking(models.Model):
    user_id = models.ForeignKey(VisitorUserProfile, on_delete=models.CASCADE, related_name='visitor_booking')
    person_count = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    room = models.ManyToManyField(
        to='Room',
        related_name='booking_room',
        blank=True,
        null=True
    )


class Room(models.Model):
    room_number = models.IntegerField()
    capacity = models.IntegerField()
    daily_rate = models.IntegerField(null=True, blank=True)
    dates = ArrayField(models.DateField(), default=list)


    def __str__(self):
        return str(self.room_number)