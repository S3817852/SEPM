from xml.dom.expatbuilder import InternalSubsetExtractor
from django.db import models
from t_account.models import Account
from t_room.models import Room

# Create your models here.
class RentContract(models.Model):
    account_id      = models.ForeignKey(Account, on_delete=models.CASCADE)
    room_id         = models.ForeignKey(Room, on_delete=models.CASCADE)
    status_Active   = models.BooleanField(default=True)
    start_Date      = models.DateField()
    end_Date        = models.DateField()
    end_Date_Actual = models.DateField()
    num_Tenants     = models.IntegerField()
    internet_Yes    = models.BooleanField()
    tv_Yes          = models.BooleanField()

class Bill(models.Model):
    rent_Contract_id    = models.ForeignKey(RentContract, on_delete=models.CASCADE)
    room_Price          = models.FloatField(null=False)
    electric_Old        = models.FloatField(null=False)
    electric_New        = models.FloatField(null=False)
    water_Old           = models.FloatField(null=False)
    water_New           = models.FloatField(null=False)
    start_Date          = models.DateField(null=False)
    end_Date            = models.DateField(null=False)
    internet            = models.FloatField(null=False)
    tv                  = models.FloatField(null=False)
    other               = models.FloatField(null=False)
    total               = models.FloatField(null=False)