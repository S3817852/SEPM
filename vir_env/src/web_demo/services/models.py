from django.db import models
from django.contrib import admin
from user.models import Userprofile

# Create your models here.
class MonthlyEW(models.Model):
    account = models.ForeignKey(Userprofile, null=True, on_delete=models.CASCADE)
    # account = models.TextField()
    tenant = models.TextField()
    electricity_consumption = models.IntegerField()
    electricity_cost = models.IntegerField()
    water_consumption = models.IntegerField()
    water_cost = models.IntegerField()
    month = models.TextField(blank=True)
    year = models.TextField(blank=True)

class EW(admin.ModelAdmin):
    list_display = ['id', 'month','year']
    list_filter = ['month','year']
    search_fields = ['month','year']


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_read = models.BooleanField(default=False, null=True)

    created_by = models.ForeignKey(Userprofile, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title