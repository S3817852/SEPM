from django.urls import path, include
from .views import room_services, room_services_details

urlpatterns = [
    path('', room_services, name='room_services'),
    path('details/', room_services_details, name='room_services_details'),
    
]