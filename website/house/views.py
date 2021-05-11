from django.shortcuts import render

# Create your views here.
def house(request):
    return render(request, 'house/house.html')

def house_add(request):
    return render(request, 'house/house_add.html')

def room(request):
    return render(request, 'house/room.html')

def room_add(request):
    return render(request, 'house/room_add.html')