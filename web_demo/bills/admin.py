from django.contrib import admin

from .models import BillAndReceipts, FixedFee, RoomConsumption

# Register your models here.
admin.site.register(FixedFee)
admin.site.register(RoomConsumption)
admin.site.register(BillAndReceipts)
