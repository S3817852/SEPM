from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Account, Tenant


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UserprofileUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['image']


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
