from django.shortcuts import render
from .models import *
from .forms import FilmForm, DirectorForm, ReviewForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import psycopg2

CONNECTION = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='w6d1xp')
CURSOR = CONNECTION.cursor()



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

class HomePageView(ListView, LoginRequiredMixin):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'all_films'
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('homepage')

    def get_queryset(self): # modifying / filtering the object list queryset
        query = self.request.GET.get('query', None)
        if query:
            posts_all = Film.objects.filter(title__icontains=query)
        else:
            posts_all = Film.objects.all()

        all_films = []
        for film_object in posts_all:
            CURSOR.execute(f"SELECT director_id FROM films_film_director WHERE film_id={film_object.id}")
            director_id = CURSOR.fetchall()[0][0]
            CURSOR.execute(f"SELECT first_name, last_name AS full_name FROM films_director WHERE id={director_id}")
            director_name = CURSOR.fetchall()[0][0]

            CURSOR.execute(f"SELECT avg(rating) FROM films_review WHERE film_id={film_object.id}")
            rating = str(CURSOR.fetchall()[0][0])[:3]
            rating = rating if rating[0].isdigit() else "No Rating"
            all_films.append({
                'title': film_object.title,
                'director': director_name,
                'rating': rating
            })
        return all_films # return what will be used as the post_list
    
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/addReview.html'
    context_object_name = 'review'
    success_url = reverse_lazy('review')


class FilmDeleteView(DeleteView, UserPassesTestMixin):
    # specify the model you want to use
    model = Film
    success_url = reverse_lazy('homepage')
    template_name = "film/confirm_delete.html"

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False

class FavoriteFilmView(View):
    model = Film
    success_url = reverse_lazy('homepage')
    template_name = "film/confirm_favorite.html"
    def post(self):
        film_id = self.request.POST.get('film_id')
        film = Film.objects.get(id=film_id)
        user_favorites = request.user.userprofile.favorite_films
        if film in user_favorites.all():
            user_favorites.remove(film)

