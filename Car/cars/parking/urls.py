
from django.urls import path

from . import views

app_name = 'cars'
urlpatterns = [
    # домашняя страница
    path('', views.index, name = 'parking'),
    path('parking/', views.parking, name = 'park'),
    path('new_parkin/', views.new_parkin, name = 'new_park'),
]