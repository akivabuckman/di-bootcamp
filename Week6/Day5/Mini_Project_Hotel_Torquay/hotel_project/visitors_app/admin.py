from django.contrib import admin

from .models import Booking, Room, VisitorUserProfile

admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(VisitorUserProfile)