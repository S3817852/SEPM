from django.urls import path, include
from .views import bill_receipts

urlpatterns = [
    path('', bill_receipts, name='bill_receipts'),
    
]