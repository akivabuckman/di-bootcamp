from .models import Person
from django import forms


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'phone_number']