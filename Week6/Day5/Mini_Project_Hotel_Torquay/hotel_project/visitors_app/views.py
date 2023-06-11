from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.views import LoginView


def visitor_home_page(request):
    context = {
        'user': request.user
    }
    return render(request, 'info_page.html', context)


class RegisterView(CreateView):
    form_class = RegisterForm
    model = User
    template_name = 'visitor-register.html'
    success_url = reverse_lazy('visitor-login')


class CustomLoginView(LoginView):
    success_url = reverse_lazy('info-page')
