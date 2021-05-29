from tenant.models import Tenant
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from userprofile.models import Userprofile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import UpdateTenantForm, AddTenantForm
from django.contrib import messages

# Create your views here.
def tenant(request):
    tenant = Tenant.objects.filter(is_rented = True)
   
    return render(request, 'tenant/tenant.html', {'tenants': tenant})

def add_tenant(request):
    form = AddTenantForm()
    if request.method == 'POST':
        form = AddTenantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"New tenant is added successfully")
            return redirect('/tenant/')
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, 'tenant/tenant_add.html', context)

def update_tenant(request, pk):
    tenant = Tenant.objects.get(id = pk)
    form = UpdateTenantForm(instance = tenant)
    if request.method == 'POST':
        form = UpdateTenantForm(request.POST, instance= tenant)
        if form.is_valid:
            form.save()
            # tenant_name = form.cleaned_data.get('name')
            messages.success(request,  "Tenant's information is updated successfully")
            return redirect('/tenant/')

    context = {'form': form}
    return render(request, 'tenant/tenant_update.html', context)

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