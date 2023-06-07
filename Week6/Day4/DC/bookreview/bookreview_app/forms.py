from django import forms
from .models import BookReview
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class SearchForm(forms.Form):
    query = forms.CharField(max_length=20)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = '__all__'

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']