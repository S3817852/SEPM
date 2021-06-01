from django import forms
from django.db import models
from django.db.models import fields
from .models import RoomService

class RequestPost(forms.ModelForm):
    class Meta:
        model = RoomService
        fields = ['service_subject' ,'description','status', 'image']

class UpdateRoomService(forms.ModelForm):
    class Meta:
        model= RoomService
        fields = ['status']
