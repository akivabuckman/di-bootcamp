from django.contrib import admin
from django.urls import path
import gifs.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage),
    path('add_new_gif/', views.add_new_gif),
    # path('add_category/', views.add_category_view),
    path('category/<int:category_id>', views.category),
    path('categories/', views.categories),
    path('gif/<int:gif_id>', views.gif)
]
