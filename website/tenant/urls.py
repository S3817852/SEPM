from django.urls import path, include
from .views import tenant, add_new_tenant

urlpatterns = [
    path('', tenant, name='tenant'),
    path('signup', add_new_tenant, name='add_new_tenant')
]