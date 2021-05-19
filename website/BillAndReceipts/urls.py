from django.urls import path, include
from .views import bill_receipts, bill_receipts_add, bill_receipts_paid, bill_receipts_processing

urlpatterns = [
    path('', bill_receipts, name='bill_receipts'),
    path('add/', bill_receipts_add, name='bill_receipts_add'),
    path('paid/', bill_receipts_paid, name='bill_receipts_paid'),
    path('processing/', bill_receipts_processing, name='bill_receipts_processing'),
]