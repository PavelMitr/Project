
from django.urls import path

from . import views

app_name = 'cars'
urlpatterns = [
    # домашняя страница
    path('', views.index, name = 'parking'),
    path('parking/', views.parking, name = 'park'),
    path('parking/<int:park_id>', views.parkingq, name = 'park_id'),
    path('parking/new_parkin/', views.new_parkin, name = 'new_park'),
    path('parking/<int:pk>/edit', views.edit_park , name = 'edit_park'),
    path('parking/<int:par_id>/delete', views.delete , name = 'delete'),
]