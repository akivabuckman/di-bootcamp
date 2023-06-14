from django.contrib import admin
from django.urls import path
from person_app.views import byphone, byname, search
from admin_app.views import admin_search


urlpatterns = [
    path('admin_app/', admin.site.urls),
    path('persons/phonenumber/<int:phone_number>', byphone),
    path('persons/name/<str:name>', byname),
    path('search', search),
    path('search_admin/', admin_search)
]
