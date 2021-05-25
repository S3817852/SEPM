from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from userprofile.models import Userprofile
from django.urls import reverse

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

    # def get_absolute_url(self):
    #     return reverse("bill_receipts_processing",kwargs={"id": self.id})

    def get_absolute_url(self):
        return reverse("owner_bill_receipts_processing",kwargs={"year": self.year, "month": self.month})

    def get_bill_detail_url(self):
        return reverse("owner_bill_detail",kwargs={"id": self.id})