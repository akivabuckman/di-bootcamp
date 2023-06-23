from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from visitors_app.models import Booking
import datetime



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'duration': forms.HiddenInput(),
            'price': forms.HiddenInput(),
            'room': forms.HiddenInput(),
            'start_date': forms.SelectDateWidget(),
            'end_date': forms.SelectDateWidget()
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        person_count = cleaned_data.get('person_count')
        if start_date and end_date and start_date < datetime.date(2023,7,1) or end_date < datetime.date(2023,7,1) \
                or start_date > datetime.date(2023,12,31) or end_date > datetime.date(2023,12,31):
            self.add_error('end_date', "Dates must be between July 1 and Dec 31 2023")
        if start_date and end_date and end_date <= start_date:
            self.add_error('end_date', "End date must be after the start date.")
        if 1 > person_count or 5 < person_count:
            self.add_error('person_count', "We only have rooms for 2-4 people.")
        return cleaned_data