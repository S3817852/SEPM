from django.db import models
from userprofile.models import Userprofile
from django.db.models.deletion import CASCADE

# Create your models here.
class Tenant(models.Model):
    tenant_id = models.ForeignKey(Userprofile, on_delete=CASCADE , null=True)
    start_date = models.DateField( auto_now_add=False,null=True)
    end_date = models.DateField(auto_now_add=False, auto_now= False,null=True)
    is_rented = models.BooleanField(default=False, null=True)