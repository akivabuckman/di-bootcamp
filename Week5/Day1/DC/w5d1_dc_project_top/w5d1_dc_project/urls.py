
from django.contrib import admin
from django.urls import path
from w5d1_dc_app.views import show_list, show_person

urlpatterns = [
    path('admin/', admin.site.urls),
    path('people', show_list),
    path('people/<id>', show_person)
]
