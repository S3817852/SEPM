from django import forms
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from userprofile.models import Userprofile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def tenant(request):
    tenant = Userprofile.objects.filter(is_owner = False)
    for instance in tenant:
        print(instance.id)
    # if( not request.user.userprofile.is_owner):
    #     print("a")
    return render(request, 'tenant/tenant.html', {'tenants': tenant})

def add_new_tenant(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # user = form.save()
            form.save()
            print('here')
            # account_type = request.POST.get('account_type', 'owner')

            # if account_type == 'owner':
            #     userprofile = Userprofile.objects.create(user=user, is_owner=True)
            #     userprofile.save()
            # else:
            #     userprofile = Userprofile.objects.create(user=user)
            #     userprofile.save()

            # login(request, user)

            return redirect(tenant)
    else:
        form = UserCreationForm()

    return render(request, 'tenant/signup.html', {'form': form})

    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)

    #     if form.is_valid():
    #         user = form.save()

    #         account_type = request.POST.get('account_type', 'owner')

    #         if account_type == 'owner':
    #             userprofile = Userprofile.objects.create(user=user, is_owner=True)
    #             userprofile.save()
    #         else:
    #             userprofile = Userprofile.objects.create(user=user)
    #             userprofile.save()

    #         login(request, user)

    #         return redirect(frontpage)
    # else:
    #     form = UserCreationForm()

    # return render(request, 'core/signup.html', {'form': form})