from django.urls import path, include
from .views import bill_receipts, bill_receipts_add, bill_receipts_paid, bill_receipts_processing, owner_bill_receipts_processing, owner_bill_detail

urlpatterns = [
    path('', bill_receipts, name='bill_receipts'),
    path('add/', bill_receipts_add, name='bill_receipts_add'),
    path('paid/', bill_receipts_paid, name='bill_receipts_paid'),
    path('processing/<int:id>/', bill_receipts_processing, name='bill_receipts_processing'),
    path('detail/<int:id>/', owner_bill_detail, name='owner_bill_detail'),
    path('monthly/<int:year>/<str:month>/', owner_bill_receipts_processing, name='owner_bill_receipts_processing'),
]