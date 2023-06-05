from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import UserProfile
from django.db.models import Q
from django.contrib.auth import logout
from django.shortcuts import redirect




class Signup(CreateView):
    form_class = RegisterForm
    model = User
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class ProfileView(ListView):
    model = UserProfile
    template_name = 'profile.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        given_id = self.kwargs['pk']
        queryset = queryset.filter(id=given_id)
        return queryset

def logout_view(request):
    logout(request)
    return redirect('homepage')