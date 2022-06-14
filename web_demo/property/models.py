from operator import mod

from account.models import Account
from django.db import models


# Create your models here.
class House(models.Model):
    owner_id = models.ForeignKey(Account, on_delete= models.CASCADE)
    address = models.CharField(max_length=1000)
    


class Room(models.Model):
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    is_rented = models.BooleanField()
