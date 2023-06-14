from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib import admin
from .forms import AdminForm

# Create your models here.
class PersonAdmin(admin.ModelAdmin):
    form = AdminForm

