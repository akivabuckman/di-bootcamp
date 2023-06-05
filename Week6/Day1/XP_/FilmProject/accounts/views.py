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
    context_object_name = 'profile_list'

    def get_queryset(self):  # modifying / filtering the object list queryset
        query = self.request.GET.get('query', None)
        if query:
            users_all = UserProfile.objects.filter(Q(id=id))
        else:
            users_all = UserProfile.objects.all()
        return users_all  # return what will be used as the post_list
def logout_view(request):
    logout(request)
    return redirect('homepage')