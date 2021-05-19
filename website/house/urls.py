from django.urls import path, include
from .views import house, house_add, room, room_add

urlpatterns = [
    path('', house.as_view(), name='house'),
    path('add', house_add, name='house_add'),
    path('room', room, name='room'),
    path('room/add/', room_add, name='room_add'),
    
]