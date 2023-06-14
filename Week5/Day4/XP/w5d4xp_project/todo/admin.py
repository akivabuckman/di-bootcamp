from django.contrib import admin
from todo.models import Todo, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Todo)