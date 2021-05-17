from django.db import models

# Create your models here.
class MonthlyEW(models.Model):
    account = models.TextField()
    tenant = models.TextField()
    electricity_consumption = models.IntegerField()
    electricity_cost = models.IntegerField()
    water_consumption = models.IntegerField()
    water_cost = models.IntegerField()