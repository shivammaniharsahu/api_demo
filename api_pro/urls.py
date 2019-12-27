from django.urls import include, path
from rest_framework import routers

from django.contrib import admin


urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
]