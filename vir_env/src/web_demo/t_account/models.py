from email.mime import image
from telnetlib import STATUS
from django.db import models

# Create your models here.
class Account(models.Model):
    is_Owner    = models.BooleanField(default=False)
    image       = models.ImageField(null=False)
    national_ID = models.TextField(null=False)
    DoB         = models.DateField(null=False)