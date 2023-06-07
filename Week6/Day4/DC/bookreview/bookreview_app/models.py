from django.db import models
from django.contrib.auth.models import User




class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    description = models.TextField()
    page_count = models.IntegerField()
    categories = models.CharField(max_length=50)
    thumbnail_url = models.URLField()
    def __str__(self):
        return self.title

class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    review_text = models.TextField()
