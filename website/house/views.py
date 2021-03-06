from userprofile.models import Userprofile
from django import forms
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.base import View
from .forms import AddHouseForm, AddRoomForm
from .models import House, Room
from django.contrib import messages

# House page
class house(View):
    template_name = 'house/house.html'
   
    def get(self, request, *args, **kwargs):
        houses = House.objects.all()
        list_house_id = []
        
        # Make a list of house_id
        for house in houses:  
            list_house_id.append(house.id)
            
        # List of rooms in each house_id
        just_a_empty_list = []
        just_a_rented_list = []
        for i in list_house_id:
           just_a_empty_list.append(Room.objects.filter(house_id = i).filter(status = 'Empty'))
           just_a_rented_list.append(Room.objects.filter(house_id = i).filter(status = 'Rented'))

        context = {'empty_room': just_a_empty_list, 'rented_room': just_a_rented_list, 'houses': houses, 'list_house_id': list_house_id}
        if request.user.userprofile.is_owner:
            return render(request, self.template_name, context)
        
# Add new house 
def house_add(request):
    form = AddHouseForm()
    if request.method == 'POST':
        form = AddHouseForm(request.POST)
        if form.is_valid:
            form.save()
            house_name = form.cleaned_data.get('name')
            messages.success(request, house_name + " is created successfully")
            
            return redirect('/house/')

    context = {'form': form}
    return render(request, 'house/house_add.html', context)

# Update a specific house
def house_update(request,pk):
    house = House.objects.get(id = pk)
    form = AddHouseForm(instance = house)
    if request.method == 'POST':
        form = AddHouseForm(request.POST, instance= house)
        if form.is_valid:
            form.save()
            house_name = form.cleaned_data.get('name')
            messages.success(request, house_name + " is updated successfully")
            return redirect('/house/')

    context = {'form': form}
    return render(request, 'house/house_update.html', context)

# Delete a specific house
def house_delete(request, id):
    house = House.objects.get(id = id)
    if request.method == 'POST':
        house.delete()
        messages.success(request, "House is deleted successfully")
        return redirect('/house/')

    context = {'house': house}
    return render(request, 'house/house_delete.html', context)

# Room page
def room(request, id):
    tenant_ids = Userprofile.objects.filter(is_owner = False)
    list_tenant_id = []

    # Make a list of house_id
    for tenant in tenant_ids:  
        list_tenant_id.append(tenant.id)
    
    for i in list_tenant_id:
        print(i)

    rooms = Room.objects.filter(house_id = id)
    
    # tenant_id = Userprofile.objects.filter()
    for i in rooms:
        if i.tenant_id:
            print(i.tenant_id)

    return render(request, 'house/room.html', context={'rooms': rooms, 'house_id': id})

# Add new rooms
def room_add(request, pk):
   
    form = AddRoomForm()
    if request.method == 'POST':
        form = AddRoomForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "New room is added successfully")
            return redirect(reverse('room', kwargs={'id': pk} ))

    context = {'form': form, 'house_id':id}
    
    return render(request, 'house/room_add.html', context)

# Update a specific room
def room_update(request,house_id, pk):
    room = Room.objects.get(id = pk)
    form = AddRoomForm(instance = room)
    if request.method == 'POST':
        form = AddRoomForm(request.POST, instance = room)
        if form.is_valid:
            form.save()
            messages.success(request, "Room is updated successfully")
            return redirect(reverse('room', kwargs={'id':house_id} ))

    context = {'form': form}
    
    return render(request, 'house/room_add.html', context)

# Delete a specific room
def room_delete(request,house_id, pk):
    houses = House.objects.all()
    list_house_id = []

    # Make a list of house_id
    for house in houses:  
        list_house_id.append(house.id)

    # Find house_id of room has ID is PK
    house_id = 0
    room = Room.objects.get(id = pk)
    a = []
    for i in list_house_id:
       a =  Room.objects.filter(house_id = i)
       if room in a:
           house_id = i
    
    
    if request.method == 'POST':
        room.delete()
        messages.success(request, "Room is deleted successfully")
        return redirect(reverse('room', kwargs={'id':house_id} ))

    context = {'room': room, 'house_id':house_id }
    return render(request, 'house/room_delete.html', context)