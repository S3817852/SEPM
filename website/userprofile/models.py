from django.contrib.auth.models import User
from django.db import models
from announcement.models import Announcement
from django.urls import reverse

# from job.models import Application, Job

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=50, null=True)
    dob = models.DateField(null=True, max_length=8)
    is_owner = models.BooleanField(default=False)
    image = models.ImageField(null = True, blank = True, upload_to = 'images/')


    def get_absolute_url(self):
        return reverse("account_update",kwargs={"id": self.id})

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])

class ConversationMessage(models.Model):
    announcement = models.ForeignKey(Announcement, related_name='conversationmessages', on_delete=models.CASCADE)
    content = models.TextField()

    created_by = models.ForeignKey(User, related_name='conversationmessages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']