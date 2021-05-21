from django.urls import path, include
from .views import house, house_add, room, room_add, house_update, house_delete, room_update, room_delete

urlpatterns = [
    path('', house.as_view(), name='house'),
    path('add', house_add, name='house_add'),
    path('room/<int:id>/', room, name='room'),
    path('room/<int:pk>/add/', room_add, name='room_add'),
    path('update/<int:pk>', house_update, name='house_update'),
    path('delete/<int:id>', house_delete, name='house_delete'),
    path('room/<int:house_id>/update/<int:pk>', room_update, name='room_update'),
    path('room/<int:house_id>/delete/<int:pk>', room_delete, name='room_delete'),
]