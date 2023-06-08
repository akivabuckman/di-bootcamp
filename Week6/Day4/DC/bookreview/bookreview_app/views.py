import psycopg2 as psycopg2
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Book, BookReview
from django.db.models import Q
from .forms import SearchForm, ReviewForm, RegisterForm
from django.urls import reverse_lazy
import psycopg2
from django.contrib.auth.models import User



CONNECTION = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='w6d4dc')

CURSOR = CONNECTION.cursor()


class BookList(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            books_all = Book.objects.filter(Q(title__icontains=query))
        else:
            books_all = Book.objects.all()
        return books_all

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_form = SearchForm()
        context['search'] = search_form
        return context


class BookView(DetailView):
    model = Book
    template_name = 'book.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = context['object'].id
        CURSOR.execute(f"SELECT avg(rating) FROM bookreview_app_bookreview WHERE book_id={book_id}")
        avg = str(CURSOR.fetchall()[0][0])[:3]
        context['avg'] = avg
        print(context)
        return context


class WriteReviewView(CreateView):
    model = BookReview
    form_class = ReviewForm
    template_name = 'write-review.html'
    success_url = reverse_lazy('books')

    def get_initial(self):
        # initial = super().get_initial()
        initial_id = self.kwargs['pk']
        CURSOR.execute(f"SELECT title FROM bookreview_app_book WHERE id={initial_id}")
        initial_title = CURSOR.fetchall()[0][0]
        print(initial_title)
        return {'title': initial_title}

class RegisterView(CreateView):
    form_class = RegisterForm
    model = User
    template_name = 'register.html'
    success_url = reverse_lazy('login')