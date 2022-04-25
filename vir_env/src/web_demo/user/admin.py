from django.contrib import admin
from .models import Userprofile, Tenant

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Tenant)
