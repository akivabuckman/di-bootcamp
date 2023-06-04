from django import forms
from .models import Rental, Customer


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'
