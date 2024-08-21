from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Allauth URLs for registration and social login
    path('', include('storage_app.urls')),  # Include storage_app URLs
]
