from django.contrib import admin
from django.urls import path
from info.views import families, animals

urlpatterns = [
    path('admin/', admin.site.urls),
    path('family/<fam_id>', families),
    path('animal/<animal_id>', animals)
]
