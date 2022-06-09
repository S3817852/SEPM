from tokenize import Double
from django.db import models

# Create your models here.
class Account(models.Model):
    is_Owner    = models.BooleanField()
    image       = models.ImageField()
    national_ID = models.TextField()
    DoB         = models.DateField()

