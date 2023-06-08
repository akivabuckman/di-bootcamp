from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('visitors/', include('visitors_app.urls')),
    path('staff/', include('staff_app.urls')),
]
