from django import forms

from .models import House, Room

class AddHouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name', 'address']

class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['house_id', 'tenant_id', 'rental_fee', 'status']



