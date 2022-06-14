from django.contrib import admin

# Register your models here.
from .models import Account, RentContract, Tenant

# Register your models here.
admin.site.register(Account)
admin.site.register(Tenant)
admin.site.register(RentContract)

