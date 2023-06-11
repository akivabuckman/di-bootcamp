from django.contrib import admin

from .models import Vacancy, Booking, Room, VisitorUserProfile

admin.site.register(Vacancy)
admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(VisitorUserProfile)