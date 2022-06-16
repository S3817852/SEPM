from django.urls import include, path

from .views import (house_add, house_delete, house_page, house_update, room,
                    room_add, room_delete, room_update)

urlpatterns = [
    # path('', house.as_view(), name='house'),
    path('', house_page, name='house'),
    path('add', house_add, name='add_house'),
    path('room/<int:id>/', room, name='room'),
    path('room/<int:pk>/add/', room_add, name='room_add'),
    path('update/<int:pk>', house_update, name='house_update'),
    path('delete/<int:id>', house_delete, name='house_delete'),
    path('room/<int:house_id>/update/<int:pk>', room_update, name='room_update'),
    path('room/<int:house_id>/delete/<int:pk>', room_delete, name='room_delete'),
]
