from django.shortcuts import render, redirect
from .models import Userprofile
from django.contrib.auth.models import User
from .forms import UserprofileUpdateForm
from django.contrib import messages

# Create your views here.
def account(request):
    if request.user.userprofile.is_owner:
        userprofile = Userprofile.objects.get(id = request.user.id)
        
        return render(request, "userprofile/O_account.html", {'userprofile': userprofile})
        #yy-mm-dd
    else:
        userprofile = Userprofile.objects.get(user = request.user)
        
        return render(request, 'userprofile/T-account.html', {'userprofile': userprofile})

def account_update(request, id):
    if request.user.userprofile.is_owner:
        userprofile = Userprofile.objects.get(id = id)
        form = UserprofileUpdateForm(instance = userprofile)
        if request.method == 'POST':
            form = UserprofileUpdateForm(request.POST, instance= userprofile)
            if form.is_valid:
                form.save()
                messages.success(request, "Account is updated successfully")
                return redirect('/account/')

        context = {'form': form}
        return render(request, "userprofile/O_account_update.html", context)
    else:
        userprofile = Userprofile.objects.get(id = id)
        form = UserprofileUpdateForm(instance = userprofile)
        if request.method == 'POST':
            form = UserprofileUpdateForm(request.POST, instance= userprofile)
            if form.is_valid:
                form.save()
                messages.success(request, "Account is updated successfully")
                return redirect('/account/')

        context = {'form': form}
        return render(request, "userprofile/T-account-update.html", context)