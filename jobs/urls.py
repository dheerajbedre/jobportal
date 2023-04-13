from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tpo/', admin.site.urls),
    path('', include('jobsapp.urls')),
    path('', include('accounts.urls')),
]
