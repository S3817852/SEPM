from account.models import Account
from django import forms

from .models import House, Room


class AddHouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['owner_id', 'address']

    # def __init__(self, user=None, **kwargs):
    #     super(AddHouseForm, self).__init__(**kwargs)
        
    #     self.fields['owner_id'].queryset  = Account.objects.filter(user=user)
class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['house_id', 'price', 'is_rented']



