from django.contrib import admin
from django.urls import path
from bookreview_app.views import BookList, BookView, WriteReviewView
from django.contrib.auth import views
from bookreview_app.views import RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookList.as_view(), name='books'),
    path('book/<int:pk>', BookView.as_view(), name='book'),
    path('write-review/<int:pk>', WriteReviewView.as_view(), name='write-review'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
