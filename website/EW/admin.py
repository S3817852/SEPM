from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import MonthlyEW

# Register your models here.
@admin.register(MonthlyEW)
class EW(ImportExportModelAdmin):
    list_display = ('id','account','tenant','electricity_consumption','electricity_cost','water_consumption','water_cost')