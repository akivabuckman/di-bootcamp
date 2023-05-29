
from django.contrib import admin
from django.urls import path
from person_app.views import byphone, byname


urlpatterns = [
    path('admin/', admin.site.urls),
    path('persons/phonenumber/<int:phone_number>', byphone),
    path('persons/name/<str:name>', byname),
]
