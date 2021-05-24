from django import forms

from .models import Userprofile

class UserprofileUpdateForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['first_name' ,'last_name','email','phone','dob']


