from operator import mod

from account.models import Account
from django.db import models
from django.urls import reverse


# Create your models here.
class House(models.Model):
    owner_id = models.ForeignKey(Account, on_delete= models.CASCADE)
    address = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse("room",kwargs={"id": self.id})
    
    def __str__(self, *args, **kwargs):
        return f'{self.id}---{self.address}'


class Room(models.Model):
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    is_rented = models.BooleanField()
    cur_electricity = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    cur_water = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    name = models.TextField(default="P001", max_length=4, null=False)

    def __str__(self, *args, **kwargs):
        return f'{self.id}---{self.name}'
