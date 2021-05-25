from django import forms

from .models import House, Room

class AddHouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'

class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

