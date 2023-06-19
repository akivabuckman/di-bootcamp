from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Booking

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'user_id': forms.HiddenInput(),
            'duration': forms.HiddenInput(),
            'price': forms.HiddenInput(),
            'room': forms.HiddenInput(),
            'start_date': forms.SelectDateWidget(),
            'end_date': forms.SelectDateWidget()
        }