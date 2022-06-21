from django.shortcuts import render


# Create your views here.
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
            # for a in i:
            #     print(a)
        return render(request, 'BillAndReceipts/bill_receipts.html',{'monthly_bill': monthly_bill, 'check_status': monthly_List})
    else:
        tenant_bill = PersonalBill.objects.filter(tenant = request.user.userprofile)
        return render(request, 'BillAndReceipts/T_billreceipt.html', {'bill': tenant_bill})
