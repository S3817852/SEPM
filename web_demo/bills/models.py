from account.models import RentContract
from django.db import models
from property.models import Room


# Create your models here.
class FixedFee(models.Model):
    electricity_fee = models.DecimalField(max_digits=10, decimal_places=3)
    water_fee = models.DecimalField(max_digits=10, decimal_places=3)
    internet_fee = models.DecimalField(max_digits=10, decimal_places=3)
    tv_fee = models.DecimalField(max_digits=10, decimal_places=3)
    other_fee = models.DecimalField(max_digits=10, decimal_places=3)

class RoomConsumption(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    electricity_consump = models.DecimalField(max_digits=10, decimal_places=3)
    water_consump = models.DecimalField(max_digits=10, decimal_places=3)
    time = models.DateField()

    def __str__(self, *args, **kwargs):
        return f'{self.id}---{self.room_id.name}---{self.time}'

class BillAndReceipts(models.Model):
    rent_contract_id = models.ForeignKey(RentContract, on_delete=models.CASCADE)
    room_price = models.DecimalField(max_digits=10, decimal_places=3)
    old_electricity = models.DecimalField(max_digits=10, decimal_places=3)
    new_electricity = models.DecimalField(max_digits=10, decimal_places=3)
    old_water = models.DecimalField(max_digits=10, decimal_places=3)
    new_water = models.DecimalField(max_digits=10, decimal_places=3)
    internet = models.DecimalField(max_digits=10, decimal_places=3)
    tv = models.DecimalField(max_digits=10, decimal_places=3)
    other = models.DecimalField(max_digits=10, decimal_places=3)
    total = models.DecimalField(max_digits=10, decimal_places=3)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()





