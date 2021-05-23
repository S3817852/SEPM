from django.urls import path, include
from .views import account, account_update

urlpatterns = [
    path('', account, name='account'),
    path('update/', account_update, name='account_update'),
    
]