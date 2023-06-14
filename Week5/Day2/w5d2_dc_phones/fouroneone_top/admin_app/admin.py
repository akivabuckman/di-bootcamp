from django.contrib import admin
from .models import PersonAdmin
from person_app.models import Person
# Register your models here.
admin.site.register(Person, PersonAdmin)