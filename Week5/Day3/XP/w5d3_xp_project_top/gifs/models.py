from django.db import models

class Gif(models.Model):
    title = models.CharField()
    url = models.URLField()
    uploader_name = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField()
    gifs = models.ManyToManyField(Gif, blank=True, related_name='categories')

    def __str__(self):
        return self.name