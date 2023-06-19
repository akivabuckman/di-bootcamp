from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from image_share.forms import RegisterForm, ImageForm
from .models import Image

class RegisterView(CreateView):
    form_class = RegisterForm
    model = User
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class UploadImage(CreateView):
    form_class = ImageForm
    model = Image
    success_url = reverse_lazy('view')
    template_name = 'image_share/image_form.html'


class ViewImages(ListView):
    model = Image
    context_object_name = 'image_list'


class ViewSelfImages(ListView):
    model = Image
    context_object_name = 'image_list'
    template_name = 'image_share/viewSelf.html'

    def get_queryset(self):
        current_user = super().get_queryset()[0].user.id
        objects = Image.objects.filter(user=current_user)
        return objects