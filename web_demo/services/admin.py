from django.contrib import admin
from .models import MonthlyEW, EW, Announcement

# Register your models here.
admin.site.register(MonthlyEW, EW)
admin.site.register(Announcement)
