from django.contrib.auth.models import User
from django.db import models
from announcement.models import Announcement

# from job.models import Application, Job

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])

class ConversationMessage(models.Model):
    announcement = models.ForeignKey(Announcement, related_name='conversationmessages', on_delete=models.CASCADE)
    content = models.TextField()

    created_by = models.ForeignKey(User, related_name='conversationmessages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']