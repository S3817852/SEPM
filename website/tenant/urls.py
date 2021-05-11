from django.urls import path, include
from .views import tenant

urlpatterns = [
    path('', tenant, name='tenant'),
    
    
]