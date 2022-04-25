from dataclasses import fields
from PIL import Image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
    image = models.ImageField(default='default_user.jpg', upload_to='profile_pics')

    def __str__(self) -> str:
        return f'{self.user.username} Profile'

    # Auto-resize the input image from users
    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Tenant(models.Model):
    tenant_id = models.ForeignKey(Userprofile, on_delete=models.CASCADE , null=True)
    start_date = models.DateField( auto_now_add=False,null=True)
    end_date = models.DateField(auto_now_add=False, auto_now= False,null=True)
    is_rented = models.BooleanField(default=True, null=True)