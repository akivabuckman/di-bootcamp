import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_project.settings')
django.setup()
from datetime import date, timedelta
import visitors_app.models as models
import random
import json



def create_roomdates():
    ROOM_COUNT = 50  # I decided the hotel has 50 rooms
    START = date(2023, 7, 1)
    END = date(2023, 12, 31)
    date_list = [START + timedelta(days=i) for i in range((END - START).days + 1)]

    for room in range(ROOM_COUNT):
        capacity = random.choice([2, 3, 4])
        for day in date_list:
            r = models.RoomDate(room_number=room + 101,
                                capacity=capacity,
                                daily_rate=capacity * 100,
                                available=True,
                                date=day)
            r.save()

def create_rooms():
    ROOM_COUNT = 50  # I decided the hotel has 50 rooms
    START = date(2023, 7, 1)
    END = date(2023, 12, 31)
    date_list = [START + timedelta(days=i) for i in range((END - START).days + 1)]
    for room in range(ROOM_COUNT):
        capacity = random.choice([2, 3, 4])
        r = models.Room(room_number=room + 101,
                            capacity=capacity,
                            daily_rate=capacity * 100,
                            dates=date_list)
        r.save()

