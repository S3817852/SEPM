from django import forms
from django.db import models
from .models import RoomService

class RequestPost(forms.ModelForm):
    class Meta:
        model = RoomService
        fields = ('service_subject' ,'description', 'image')
