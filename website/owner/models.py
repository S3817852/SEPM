from django.db import models
from django.urls import reverse

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    
    dob = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return   reverse("details", kwargs= {"id": self.id})   #f"./{self.id}/"s
