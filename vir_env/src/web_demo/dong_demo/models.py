from django.db import models

# Create your models here.
class DongInfo(models.Model):
    name = models.TextField(blank=True)
    age = models.IntegerField()
    