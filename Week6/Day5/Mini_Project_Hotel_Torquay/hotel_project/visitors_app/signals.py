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

@receiver(signal=post_save, sender=Booking)
def remove_dates(sender, instance, created, **kwargs):
    if created:
        pass
        # CURSOR.execute(f"SELECT room_id FROM visitors_app_booking_room WHERE booking_id = {instance.id}")
        # room_id = CURSOR.fetchone()
        # print(room_id)
        # CURSOR.execute(f"SELECT dates FROM visitors_app_room WHERE id = {room_id}")
        # pre_dates = CURSOR.fetchall()
        # print(pre_dates)
        # print('XXXXXXXXXXXXXXXXX')

# @receiver(signal=post_save, sender=User)
# def attach_user_group(sender, instance, created, **kwargs):
#     if created:
#         if not instance.is_staff:
#             group = Group.objects.get(name='regular')
#             instance.groups.add(group)
#     else:
#         print("EXISTING")
#         if instance.is_staff:
#             group = Group.objects.get(name='regular')
#             print("GROUP", group)
#             group.user_set.remove(instance)