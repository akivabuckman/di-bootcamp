from django.db import models
from django.contrib.auth.models import User

class VisitorUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='visitor_user')
    def __str__(self):
        return f'Profile: {self.user.username}'