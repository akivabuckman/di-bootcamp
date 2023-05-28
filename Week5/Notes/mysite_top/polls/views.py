from datetime import date
from django.shortcuts import render
from django.http import HttpResponse

def posts(request):
    today = date.today()
    title = 'MY FIRST SITE'
    content = 'bla blahahah'
    author = 'joe'

    context = {
        'time': today,
        'title': title,
        'content': content,
        'author': author
    }
    return render(request, 'posts.html', context)

def profile(request):
    user_info = {
        'fname': 'akiva',
        'lname': 'buckman',
        'hobbies': ['python', 'guitar'],
        'gender': 'm',
    }

    return render(request, 'profile_user.html', user_info)