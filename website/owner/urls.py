from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_details_view, name='detail'),
    path('create/', views.product_create_view, name='create')
]