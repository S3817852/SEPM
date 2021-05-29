from django.urls import path, include
from .views import tenant, add_new_tenant, update_tenant, add_tenant

urlpatterns = [
    path('', tenant, name='tenant'),
    path('signup', add_new_tenant, name='add_new_tenant'),
    path('add', add_tenant, name='add_tenant'),
    path('update/<int:pk>/', update_tenant, name='update_tenant')
]