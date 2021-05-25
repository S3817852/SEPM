from django.db import models
from django.urls import path, include
from .views import index


urlpatterns = [
    path('', index, name='messages'),
    
    
] 