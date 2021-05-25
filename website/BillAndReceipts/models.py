from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from userprofile.models import Userprofile

# Create your models here.
class PersonalBill(models.Model):
    BILL_STATUS = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid')
    )

    tenant = models.ForeignKey(Userprofile, null=True, on_delete=CASCADE)
    
    electricity_consumption = models.IntegerField( null=True)
    electricity_cost = models.IntegerField( null=True)
    water_consumption = models.IntegerField( null=True)
    water_cost = models.IntegerField( null=True)
    created_at = models.DateTimeField( null=True, auto_now_add=True)
    month = models.CharField(blank=True, max_length=50)
    year = models.CharField(blank=True, max_length=50)
    status = models.CharField(max_length=50, null=True, choices=BILL_STATUS)