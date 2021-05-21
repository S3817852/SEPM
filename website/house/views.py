from house.admin import House_Id
from django import forms
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.base import View
from .forms import AddHouseForm, AddRoomForm
from .models import House, Room



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
        

def house_add(request):
    form = AddHouseForm()
    if request.method == 'POST':
        form = AddHouseForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/house/')

    context = {'form': form}
    return render(request, 'house/house_add.html', context)

def house_update(request,pk):
    house = House.objects.get(id = pk)
    form = AddHouseForm(instance = house)
    if request.method == 'POST':
        form = AddHouseForm(request.POST, instance= house)
        if form.is_valid:
            form.save()
            return redirect('/house/')

    context = {'form': form}
    return render(request, 'house/house_update.html', context)

def house_delete(request, id):
    house = House.objects.get(id = id)
    if request.method == 'POST':
        house.delete()
        return redirect('/house/')

    context = {'house': house}
    return render(request, 'house/house_delete.html', context)

def room(request, id):
    rooms = Room.objects.filter(house_id = id)

    return render(request, 'house/room.html', context={'rooms': rooms, 'house_id': id})

def room_add(request, pk):
   
    form = AddRoomForm()
    if request.method == 'POST':
        form = AddRoomForm(request.POST)
        if form.is_valid:
            form.save()
            # return redirect('/house/room/')
            return redirect(reverse('room', kwargs={'id': pk} ))

    context = {'form': form, 'house_id':id}
    
    return render(request, 'house/room_add.html', context)

def room_update(request,house_id, pk):
    room = Room.objects.get(id = pk)
    form = AddRoomForm(instance = room)
    if request.method == 'POST':
        form = AddRoomForm(request.POST, instance = room)
        if form.is_valid:
            form.save()
            return redirect(reverse('room', kwargs={'id':house_id} ))

    context = {'form': form}
    
    return render(request, 'house/room_add.html', context)

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
        return redirect(reverse('room', kwargs={'id':house_id} ))

    context = {'room': room, 'house_id':house_id }
    return render(request, 'house/room_delete.html', context)