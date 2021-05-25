from django.urls import path, include
from .views import ew, ew_add, ew_month

urlpatterns = [
    path('', ew, name='ew'),
    path('add/', ew_add, name='ew_add'),
    path('monthly/<int:year>/<str:month>/', ew_month, name='ew_month'),
]