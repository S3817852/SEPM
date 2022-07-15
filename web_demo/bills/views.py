from django.shortcuts import render
from account.models import RentContract
from .models import FixedFee, RoomConsumption
from property.models import Room

# Create your views here.
def calculate_bill_view(request, *args, **kwargs):
    room_property = Room.objects.get(id=1)
    # room_property.price
    # room_property.cur_electricity
    # room_property.cur_water
    
    room_consump = RoomConsumption.objects.get(room_id=1, time="2022-01-31")
    # room_consump.electricity_consump
    # room_consump.water_consump
    # room_consump.time
    
    fixed_fee = FixedFee.objects.get(id=1)
    # fixed_fee.electricity_fee
    # fixed_fee.water_fee
    # fixed_fee.internet_fee
    # fixed_fee.tv_fee
    # fixed_fee.other_fee

    rent_contract = RentContract.objects.get(room_id=1, account_id=2)
    
    # rent_contract.start_date

    rent_contract_id = rent_contract.id
    room_price = room_property.price
    old_electricity = room_property.cur_electricity
    new_electricity = room_consump.electricity_consump
    total_electricity = (room_consump.electricity_consump-room_property.cur_electricity)*3000
    old_water = room_property.cur_water
    new_water = room_consump.water_consump
    total_water = (room_consump.water_consump-room_property.cur_water)*9000
    if rent_contract.internet_usage:
        internet = fixed_fee.internet_fee
    if rent_contract.tv_usage:
        tv = fixed_fee.tv_fee
    other = fixed_fee.other_fee*rent_contract.num_tenants
    total = room_price+total_electricity+total_water+internet+tv+other
    start_date = rent_contract.start_date
    end_date = room_consump.time

    print(f"Rent Contract ID: {rent_contract_id}\nRoom Price: {room_price}\nOld Elec: {old_electricity}\nNew Elec: {new_electricity}\nTotal Elec: {total_electricity}\nOld Water: {old_water}\nNew Water: {new_water}\nTotal Water: {total_water}\nInternet: {internet}\nTV: {tv}\nOther Fee: {other}\nTOTAL: {total}\nStart Date: {start_date}\nEnd Date: {end_date}")

    return render(request, "calculate_bill.html", {})