from django import forms

from .models import Announcement

class AddAnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'description']

