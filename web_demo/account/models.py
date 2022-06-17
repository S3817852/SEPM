from django.contrib.auth.models import User
from django.db import models
from PIL import Image


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
    image = models.ImageField(default='default_user.jpg', upload_to='profile_pics')
    national_id = models.TextField(blank=True)
    dob = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'

    # Auto-resize the input image from users
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Tenant(models.Model):
    tenant_id = models.ForeignKey(Account, on_delete=models.CASCADE , null=True)
    start_date = models.DateField( auto_now_add=False,null=True)
    end_date = models.DateField(auto_now_add=False, auto_now= False,null=True)
    is_rented = models.BooleanField(default=True, null=True)

class RentContract(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    room_id = models.ForeignKey("property.Room", on_delete=models.CASCADE)
    num_tenants = models.DecimalField(max_digits=2, decimal_places=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    actual_end_date = models.DateTimeField(blank=True, null=True)
    internet_usage = models.BooleanField()
    tv_usage = models.BooleanField()


