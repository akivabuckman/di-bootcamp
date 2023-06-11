from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models import F



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
    def __str__(self):
        return str(self.room_number)


class Booking(models.Model):
    visitor_id = models.ManyToManyField(VisitorUserProfile, related_name='visitor_booking')
    person_count = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    room_id = models.ForeignKey(to=Room, on_delete=models.DO_NOTHING, related_name='booking_roomid', blank=True,
                                null=True)
    # def save(self, *args, **kwargs):
    #     self.duration = F('end_date') - F('start_date')
    #     self.price = self.duration * self.

