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
    