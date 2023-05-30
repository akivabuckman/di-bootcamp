from django.shortcuts import render
from gifs.models import Gif, Category
import psycopg2

def homepage(request):
    all_gifs = Gif.objects.all()
    all_urls = [i.url for i in all_gifs]
    a = all_gifs[0].url
    context = {'all_urls': all_urls}
    print(a)
    return render(request, 'homepage.html', context)


def add_new_gif(request):
    context = {}
    return render(request, 'add_new_gif.html', context)


def add_new_category(request):
    context = {}
    return render(request, 'add_new_gif.html', context)

def category(request, category_id):
    CONNECTION = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='w5d3_xp')
    CURSOR = CONNECTION.cursor()
    CURSOR.execute(f"SELECT gif_id FROM gifs_category_gifs WHERE category_id = {category_id}")
    hits = CURSOR.fetchall()
    gif_ids = [i[0] for i in hits]
    gif_urls = []
    for i in gif_ids:
        gif_urls.append(Gif.objects.filter(id=i)[0].url)
    context = {
        'hits': hits,
        'gif_ids': gif_ids,
        'gif_urls': gif_urls,
    }
    return render(request,'category.html', context)

def categories(request):
    all_categories = Category.objects.all()
    ids = [i.id for i in all_categories]
    context = {
        'all_categories': all_categories,
        'ids': ids,
    }
    return render(request,'categories.html', context)

def gif(request, gif_id):
    result = Gif.objects.filter(id=gif_id)[0]

    context = {
        'id': gif_id,
        'name': result.title,
        'url': result.url,
        'uploader': result.uploader_name,
        'datetime': result.created_at,
    }
    return render(request,'gif.html', context)
