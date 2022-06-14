from cgi import print_exception
from datetime import date
from django.db import models
from t_house.models import House

# Create your models here.
class Room(models.Model):
    is_Rented   = models.BooleanField(default=False)
    house_id    = models.ForeignKey(House, on_delete=models.CASCADE)
    price       = models.FloatField(default=1750000) 

class FixedFee(models.Model):
    date_Update         = models.DateField(null=False)
    electric_Fee        = models.FloatField(default=2200)
    electric_Fee_Over   = models.FloatField(default=3000) 
    water_Fee           = models.FloatField(default=10000)
    water_Fee_Over      = models.FloatField(default=15000)
    internet_Fee        = models.FloatField(default=50000)
    tv_Fee              = models.FloatField(default=20000)
    other_Fee           = models.FloatField(default=12000)  

class RoomConsumption(models.Model):
    room_id         = models.ForeignKey(Room, on_delete=models.CASCADE)
    month_Year      = models.DateField(null=False)
    electric_Num    = models.IntegerField()
    water_Num       = models.IntegerField()