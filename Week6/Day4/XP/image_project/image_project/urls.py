from django.contrib import admin
from django.urls import path, include
from image_share.views import RegisterView, UploadImage, ViewImages, ViewSelfImages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', RegisterView.as_view(), name='register'),
    path('images/upload', UploadImage.as_view(), name='upload'),
    path('images/view', ViewImages.as_view(), name='view'),
    path('images/viewSelf', ViewSelfImages.as_view(), name='viewSelf')
]
