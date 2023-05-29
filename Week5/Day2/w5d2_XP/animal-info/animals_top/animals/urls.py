from django.contrib import admin
from django.urls import path
from info.views import animals, animal, families

urlpatterns = [
    path('admin/', admin.site.urls),
    path('family/<int:fam_id>', families),
    path('animal/<int:animal_id>', animal),
    path('animals/', animals)
]
