from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import BookReview


@receiver(signal=post_save, sender=User)
def create_review(sender, instance, created, **kwargs):
    if created:
        BookReview.objects.create(user=instance)
