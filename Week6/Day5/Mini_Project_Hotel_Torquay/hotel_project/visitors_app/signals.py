from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import VisitorUserProfile, Booking
import psycopg2

CONNECTION = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='w6d5mp6')
CURSOR = CONNECTION.cursor()


@receiver(signal=post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        VisitorUserProfile.objects.create(user=instance)
        instance.save()
