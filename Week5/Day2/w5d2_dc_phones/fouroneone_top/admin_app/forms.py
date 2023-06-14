from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from person_app.models import Person


class AdminForm(forms.ModelForm):
    phone_number = PhoneNumberField(widget=RegionalPhoneNumberWidget)

    class Meta:
        model = Person
        exclude = ('id',)

