from django.db import models
from django.urls import path, include
from .views import room_services, room_services_details, room_services_add


urlpatterns = [
    path('', room_services, name='room_services'),
    path('details/<int:id>/', room_services_details, name='room_services_details'),
    path('add/', room_services_add, name='room_services_add'),
    
] 