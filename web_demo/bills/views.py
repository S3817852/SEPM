from django.shortcuts import render

from .models import RoomConsumption

# Create your views here.

# Bills view
def room_consumption_view(request):
    consumption = RoomConsumption.objects.all()
    room_consumption_info = {}

    #Make a list of room consumption
    for room_consumption in consumption:
        room_consumption_info[room_consumption] = {'id':room_consumption.id, 'room':room_consumption.room_id, 'electric_consumption':room_consumption.electricity_consump,'water_consumption':room_consumption.water_consump, 'time':room_consumption.time}
    # print(room_consumption_info)
    context = {'consumption' : room_consumption_info}
    if request.user.account.is_owner:
        return render(request, 'bills/roomconsumption.html', context)
