from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Image


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'