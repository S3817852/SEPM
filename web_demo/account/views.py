from datetime import datetime

from dateutil import tz
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from property.models import Room

from .forms import (AddTenantForm, UpdateTenantForm, UserprofileUpdateForm,
                    UserSignUpForm, UserUpdateForm)
from .models import Account, RentContract, Tenant


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        register_form = UserSignUpForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Signup successfully')

            return redirect('base_page')
        else:
            for msg in register_form.error_messages:
                messages.error(request, f"{msg}: {register_form.error_messages[msg]}")
    else:
        register_form = UserSignUpForm()
    return render(request, 'core/signup.html', {'form': register_form})

@login_required
def userprofile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST ,instance=request.user)
        user_profile_form = UserprofileUpdateForm(request.POST, request.FILES, instance=request.user.account)

        if user_form.is_valid and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()

            messages.success(request, f'Updated successfully')

            return redirect('user_profile')
        else:
            for msg in user_form.error_messages:
                messages.error(request, f"{msg}: {user_form.error_messages[msg]}")

    else:
        user_form = UserUpdateForm(instance=request.user)
        user_profile_form = UserprofileUpdateForm(instance=request.user.account)
    context = {
        'u_form': user_form,
        'up_form': user_profile_form
    }

    return render(request, 'account.html', context)


@login_required
def main_page(request):
    if request.user.account.is_owner:
        messages.success(request, 'Login successfully')
        return render(request, 'core/ownermain.html',{})
    else:
        messages.success(request, 'Login successfully')
        return render(request, 'core/tenantmain.html',{})


def login_page(request, *args, **kwargs):
    return render(request, 'core/login.html', {})




def tenant_manage(request):
    rent_contracts = RentContract.objects.all()
    current_time = datetime.now().replace(tzinfo=tz.tzlocal()) 
    
    for rc in rent_contracts:

        # Check 
        if rc.actual_end_date == None:
            covert_utc_to_vn_time_end_date = rc.end_date.astimezone(tz.tzlocal())
            remain_time = covert_utc_to_vn_time_end_date - current_time

            if remain_time.days < 0:
                # Update room status
                Room.objects.filter(id=rc.room_id.id).update(is_rented=False)
                RentContract.objects.filter(id=rc.id).update(actual_end_date=rc.end_date)
                

   
    return render(request, 'tenant/tenant.html', {'rent_contracts': rent_contracts})

def add_tenant(request):
    form = AddTenantForm()
    if request.method == 'POST':
        form = AddTenantForm(request.POST)
        if form.is_valid():
            form.save()
            # Update room status when new rent contract is created
            room_id = form.cleaned_data['room_id']
            Room.objects.filter(id=room_id.id).update(is_rented=True)
            
            messages.success(request,"New tenant is added successfully")
            return redirect('/tenant/tenant')
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, 'tenant/tenant_add.html', context)

def update_tenant(request, pk):
    tenant = RentContract.objects.get(id = pk)
    form = UpdateTenantForm(instance = tenant)
    if request.method == 'POST':
        form = UpdateTenantForm(request.POST, instance= tenant)
        if form.is_valid():
            if form.cleaned_data['actual_end_date']:
                Room.objects.filter(id=form.cleaned_data['room_id'].id).update(is_rented=False)
            form.save()
            # tenant_name = form.cleaned_data.get('name')
            messages.success(request,  "Tenant's information is updated successfully")
            return redirect('/tenant/tenant')

    context = {'form': form}
    return render(request, 'tenant/tenant_update.html', context)
