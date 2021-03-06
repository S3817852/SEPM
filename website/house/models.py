from userprofile.models import Userprofile
from django.db import models
from django.db.models.deletion import CASCADE
from owner.models import Owner
from django.urls import reverse
# Create your models here.
class House(models.Model):
    # STATUS = (
    #     ('Rented_rooms', 'Rented_rooms'),
    #     ('Empty_rooms', 'Empty_rooms')
    # )

    name = models.CharField(max_length= 100)
    address = models.CharField(max_length= 200)
    # rooms = models.IntegerField()
    owner = models.ForeignKey(Userprofile, null=True, on_delete= models.SET_NULL)
    # status = models.CharField(max_length= 255, null=True, choices=STATUS)
    # is_rented = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("room",kwargs={"id": self.id})

class Room(models.Model):
    ROOM_STATUS = (
        ('Rented', 'Rented'),
        ('Empty', 'Empty')
    )

    house_id = models.ForeignKey(House, null=True, on_delete=CASCADE)
    tenant_id = models.ForeignKey(Userprofile, null=True,blank=True, on_delete=CASCADE)
    tenant_name = models.CharField(max_length= 100, null=True, blank=True)
    rental_fee = models.IntegerField(null=True)
    status = models.CharField(max_length= 255, null=True, choices=ROOM_STATUS)