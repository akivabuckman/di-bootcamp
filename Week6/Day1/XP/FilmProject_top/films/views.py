from django.shortcuts import render
from .models import *
# from .forms import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView

class HomePageView(ListView):
    model = None
    fields = None
    template_name = 'homepage.html'
    success_url = reverse_lazy('homepage')