from django.urls import path, include
from .views import ew

urlpatterns = [
    path('', ew, name='ew'),
    
    
]