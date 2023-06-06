from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.db import models
from films.models import Film


class User_New(AbstractUser):
    favorite_films = models.ManyToManyField(Film, related_name='users_favorite', blank=True)
    groups = models.ManyToManyField(Group, related_name='accounts_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='accounts_users', blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user_profile')
    favorite_films = models.ManyToManyField('films.Film', blank=True)

    def __str__(self):
        return f'Profile: {self.user.username}'
