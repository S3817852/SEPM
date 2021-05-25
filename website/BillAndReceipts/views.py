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
        monthly_List = PersonalBill.objects.all()   # Get all record in data
        # count = monthly_List.count()

        year_list = []
        month_list = []
        unique_id_list = []
        for obj in monthly_List:
            if obj.year not in year_list:
                year_list.append(obj.year)
            if obj.month not in month_list:
                month_list.append(obj.month)
                unique_id_list.append(obj.id)

        # for i in unique_id_list:
        #     print(i)

        monthly_bill = PersonalBill.objects.filter(pk__in = unique_id_list).order_by("-year")
        
        for i in monthly_bill:
            print(i)
        return render(request, 'BillAndReceipts/bill_receipts.html',{'monthly_bill': monthly_bill})
    else:
        tenant_bill = PersonalBill.objects.filter(tenant = request.user.userprofile)
        return render(request, 'BillAndReceipts/T_billreceipt.html', {'bill': tenant_bill})

def bill_receipts_add(request):
    houses = House.objects.all()
    if request.user.userprofile.is_owner:
        month = request.POST.get('billreceipt-month')
        year = request.POST.get('billreceipt-year')
        # house = request.POST.get('billreceipt-house')
        if request.method == 'POST':
            
            # Count monthly consumption
            monthly_list = MonthlyEW.objects.filter(year = year).filter(month = month)
            for bill in monthly_list:
                electricity_monthly = bill.electricity_consumption * bill.electricity_cost
                water_monthly = bill.water_consumption * bill.water_cost
                if bill.electricity_consumption > 0:
                # rooms = Room.objects.filter(house_id = house).get(tenant_id = bill.account)
                # print(rooms.rental_fee)
                    tenant_bill = PersonalBill.objects.create(tenant= bill.account, electricity_consumption = bill.electricity_consumption,
                            electricity_cost = bill.electricity_cost,water_consumption = bill.water_consumption, water_cost = bill.water_cost, 
                            month = month, year = year, status = "Unpaid" )
                    tenant_bill.save()
                    
                
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

def bill_receipts_processing(request,id):
    # if request.user.userprofile.is_owner:
    #     return render(request, 'BillAndReceipts/O_billreceipt_paymentinprogress.html')
    # else:
        processing_bill = PersonalBill.objects.get(id = id)
        tenant_room = Room.objects.get(tenant_id = processing_bill.tenant)
        total_cost = (processing_bill.electricity_cost * processing_bill.electricity_consumption) + (tenant_room.rental_fee) + (processing_bill.water_cost * processing_bill.water_consumption)
        return render(request, 'BillAndReceipts/T_billreceiptdetail_unpaid.html', {'processing_bill': processing_bill,
         'tenant_room':tenant_room,
         'total':total_cost})

def owner_bill_receipts_processing(request, year, month):
    monthly_list = PersonalBill.objects.filter(year = year).filter(month = month)
    # for i in monthly_list:
    #     tenant_bill = PersonalBill.objects.filter(tenant = i.tenant)
        
    # tenant_bill = PersonalBill.objects.get(tenant = i.tenant)
    return render(request, 'BillAndReceipts/O_billreceipt_paymentinprogress.html', {'monthly_list': monthly_list,
    })

def owner_bill_detail(request, id):
    processing_bill = PersonalBill.objects.get(id = id)
    tenant_room = Room.objects.get(tenant_id = processing_bill.tenant)
    total_cost = (processing_bill.electricity_cost * processing_bill.electricity_consumption) + (tenant_room.rental_fee) + (processing_bill.water_cost * processing_bill.water_consumption)
    return render(request, 'BillAndReceipts/O_billreceiptdetail_unpaid.html', {'processing_bill': processing_bill,
        'tenant_room':tenant_room,
        'total':total_cost})