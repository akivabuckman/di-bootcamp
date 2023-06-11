from django.db import models
from django.contrib.auth.models import User
from django.db import models


class VisitorUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='visitor_user')
    def __str__(self):
        return f'Profile: {self.user.username}'


class Vacancy(models.Model):
    date = models.DateField()


class Room(models.Model):
    room_number = models.IntegerField()
    capacity = models.IntegerField()
    rate = models.IntegerField()


class Booking(models.Model):
    visitor_id = models.ManyToManyField(VisitorUserProfile, related_name='visitor_booking')
    person_count = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField()
    price = models.IntegerField()
    room_id = models.ForeignKey(to=Room, on_delete=models.DO_NOTHING, related_name='booking_roomid',
                                limit_choices_to=[i + 1 for i in range(11)])
