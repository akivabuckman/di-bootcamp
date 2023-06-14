"""
URL configuration for bike_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rent.views import add_vehicle, view_vehicle, view_vehicles, add_rental, add_customer, view_rentals, view_rental, view_customer, view_customers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/rental/add', add_rental),
    path('rent/rental/<int:pk>', view_rental),
    path('rent/rentals/', view_rentals),
    path('rent/customer/<int:pk>', view_customer),
    path('rent/customer/', view_customers),
    path('rent/customer/add/', add_customer),
    path('rent/vehicle/', view_vehicles),
    path('rent/vehicle/<int:pk>', view_vehicle),
    path('rent/vehicle/add', add_vehicle)
]
