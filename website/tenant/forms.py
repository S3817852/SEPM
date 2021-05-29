from django.db import models
from django.db.models import fields
from django.db.models.fields import files
from .models import Tenant
from django import forms
from userprofile.models import Userprofile

class UpdateTenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = '__all__'



class AddTenantForm(forms.ModelForm):
    # tenant_id = forms.ForeignKey(Userprofile, on_delete=CASCADE , null=True)
    start_date = forms.DateField(widget=forms.TextInput(
        attrs={
            "placeholder":"Date format: yyyy-MM-dd"
        }
    ))
    end_date = forms.DateField(widget=forms.TextInput(
        attrs={
            "placeholder":"Date format: yyyy-MM-dd"
        }
    ))
    is_rented = forms.BooleanField(required=False)

    class Meta:
        model = Tenant
        fields = '__all__'
    