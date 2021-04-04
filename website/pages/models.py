from django.db import models

# Create your models here.
class Page1(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    featured = models.BooleanField()