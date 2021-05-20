from house.admin import House_Id
from django import forms
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .forms import AddHouseForm
from .models import House, Room



class house(View):
    template_name = 'house/house.html'
   
    def get(self, request, *args, **kwargs):
        houses = House.objects.all()
        all_rooms = Room.objects.all()
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
        else:
            return render(request, self.template_name, context)

def house_add(request):
    form = AddHouseForm()
    if request.method == 'POST':
        form = AddHouseForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'house/house_add.html', context)

def room(request, id):
    rooms = Room.objects.filter(house_id = id)

    return render(request, 'house/room.html', context={'rooms': rooms})

def room_add(request):
    return render(request, 'house/room_add.html')