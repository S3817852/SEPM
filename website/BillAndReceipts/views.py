from userprofile.models import Userprofile
from tenant.views import tenant
from django.shortcuts import redirect, render
from EWs.models import MonthlyEW
from house.models import House, Room
from .models import PersonalBill

# Create your views here.
def bill_receipts(request):
    if request.user.userprofile.is_owner:
        # tenant_test = Userprofile.objects.get(id = 2)
        # testing = PersonalBill.objects.create(tenant= tenant_test, electricity_consumption = 10, electricity_cost = 3800,
        # water_consumption = 100, water_cost = 4500, month = "July", year = "2020", status = "Unpaid" )
        # testing.save()
        return render(request, 'BillAndReceipts/bill_receipts.html')
    else:
        tenant_bill = PersonalBill.objects.get(tenant = request.user.userprofile)
        return render(request, 'BillAndReceipts/T_billreceipt.html', {'bill': tenant_bill})

def bill_receipts_add(request):
    houses = House.objects.all()
    if request.user.userprofile.is_owner:
        month = request.POST.get('billreceipt-month')
        year = request.POST.get('billreceipt-year')
        house = request.POST.get('billreceipt-house')
        if request.method == 'POST':
            
            # Count monthly consumption
            monthly_list = MonthlyEW.objects.filter(year = year).filter(month = month)
            for bill in monthly_list:
                electricity_monthly = bill.electricity_consumption * bill.electricity_cost
                water_monthly = bill.water_consumption * bill.water_cost
                rooms = Room.objects.filter(house_id = house).get(tenant_id = bill.account)
                print(rooms.rental_fee)
                # print(bill.account.id)
                # print(house)
                # print("elec " + str(electricity_monthly))
                # print("water " + str(water_monthly))

            
            # for i in rooms:
            #     if i.tenant_id:
            #         print(i.tenant_id.id)

        return render(request, 'BillAndReceipts/O_billreceipt_new.html', {'houses': houses})

def bill_receipts_paid(request):
    if request.user.userprofile.is_owner:
        return render(request, 'BillAndReceipts/O_billreceipt_allpaid.html')
    else:
        return render(request, 'BillAndReceipts/T_billreceiptdetail_paid.html')

def bill_receipts_processing(request):
    if request.user.userprofile.is_owner:
        return render(request, 'BillAndReceipts/O_billreceipt_paymentinprogress.html')
    else:
        return render(request, 'BillAndReceipts/T_billreceiptdetail_unpaid.html')