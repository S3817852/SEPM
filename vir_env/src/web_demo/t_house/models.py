from django.db import models
from t_account.models import Account

# Create your models here.
class House(models.Model):
    address     = models.TextField(null=False)
    owner_id    = models.ForeignKey(Account, on_delete=models.CASCADE)