from django.db import models
from django.contrib.auth.models import User

class StaffUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_user')
    def __str__(self):
        return self.user.username