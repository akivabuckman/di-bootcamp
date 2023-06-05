from django import forms
from .models import Category, Country, Film, Director, Review

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'rating': forms.RadioSelect()
        }