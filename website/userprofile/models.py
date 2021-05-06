from django.contrib.auth.models import User
from django.db import models

# from job.models import Application, Job

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])