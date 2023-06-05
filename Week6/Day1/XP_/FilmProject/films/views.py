from django.shortcuts import render
from .models import *
from .forms import FilmForm, DirectorForm, ReviewForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView


class HomePageView(ListView):
    model = None
    fields = None
    template_name = 'homepage.html'
    success_url = reverse_lazy('homepage')

class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'film/addFilm.html'
    success_url = reverse_lazy('create-film')


class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'director/addDirector.html'
    success_url = reverse_lazy('create-director')

class HomePageView(ListView):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'homepage'

    def get_queryset(self): # modifying / filtering the object list queryset

        query = self.request.GET.get('query', None)
        if query:
            posts_all = Film.objects.filter(title__icontains=query)
        else:
            posts_all = Film.objects.all()

        return posts_all # return what will be used as the post_list
    
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/addReview.html'
    context_object_name = 'review'
    success_url = reverse_lazy('review')