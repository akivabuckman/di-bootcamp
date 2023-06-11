from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import VisitorUserProfile, Booking

@receiver(signal=post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        VisitorUserProfile.objects.create(user=instance)
        instance.save()

@receiver(signal=post_save, sender=Booking)
def remove_vacancy(sender, instance, created, **kwargs):
    if created:
        print(instance)

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