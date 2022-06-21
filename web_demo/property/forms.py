from account.models import Account
from django import forms

from .models import House, Room


class AddHouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['owner_id', 'address']

    def __init__(self,*args, **kwargs):
        owner = kwargs.pop('owner')
        super().__init__(*args,**kwargs)
        self.fields['owner_id'].queryset  = Account.objects.filter(user=owner)
class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['house_id', 'price', 'is_rented']

    def __init__(self,*args, **kwargs):
        house_id = kwargs.pop('house_id')
        super().__init__(*args,**kwargs)
        self.fields['house_id'].queryset  = House.objects.filter(id=house_id)



