import datetime
from django import forms
from .models import Category, Gif
from django.db import models


class GifForm(forms.ModelForm):
    class Meta:
        model = Gif
        fields = '__all__'
