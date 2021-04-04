from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='view'),
    path('contact/', views.contact_view, name='contact'),
]