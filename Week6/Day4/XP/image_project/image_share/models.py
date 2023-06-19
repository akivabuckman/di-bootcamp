from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    file = models.URLField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_count = models.IntegerField()


