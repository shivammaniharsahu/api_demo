from django.urls import include, path

from . import views
from django.contrib import admin


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', views.api_list),
    path('api/<int:pk>/', views.api_detail),

]