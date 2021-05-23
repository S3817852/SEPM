from django.db import models
from django.urls import reverse

# Create your models here.
class MonthlyEW(models.Model):
    account = models.TextField()
    tenant = models.TextField()
    electricity_consumption = models.IntegerField()
    electricity_cost = models.IntegerField()
    water_consumption = models.IntegerField()
    water_cost = models.IntegerField()
    month = models.TextField(blank=True)
    year = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("ew_month",kwargs={"year": self.year, "month": self.month})