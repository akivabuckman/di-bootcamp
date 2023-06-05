from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = RegisterForm
    model = User
    template_name = 'register.html'
    success_url = reverse_lazy('login')
