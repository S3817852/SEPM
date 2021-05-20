from django.contrib import admin
from .models import House, Room

# Register your models here.
class House_Id(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(House, House_Id)
admin.site.register(Room)