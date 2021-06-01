from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class RoomService(models.Model):
    REQUEST_STATUS = (
        ('Done', 'Done'),
        ('Processing', 'Processing')
    )

    service_subject = models.CharField(max_length= 300)
    description = models.TextField()
    image = models.ImageField(null = True, blank = True, upload_to = 'images/')
    status = models.CharField(max_length=50 , null=True, choices=REQUEST_STATUS)

    created_at = models.DateTimeField(auto_now_add=True,null=True)
    changed_at = models.DateTimeField(auto_now=True,null=True)
    created_by = models.ForeignKey(User, related_name='service', on_delete=models.CASCADE,null=True)

    def get_absolute_url(self):
        return reverse("room_services_details",kwargs={"id": self.id})