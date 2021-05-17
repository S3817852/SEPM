from django.shortcuts import render, get_object_or_404
from .models import MonthlyEW
from .resources import EWresources
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

# Create your views here.
def ew(request):
    monthly_List = MonthlyEW.objects.all()   # Get all record in data
    
    year_list = []
    month_list = []
    unique_id_list = []
    for obj in monthly_List:
        if obj.year not in year_list:
            year_list.append(obj.year)
        if obj.month not in month_list:
            month_list.append(obj.month)
            unique_id_list.append(obj.id)

    monthly_list = MonthlyEW.objects.filter(pk__in = unique_id_list)
    return render(request, 'EW/ew.html',{'monthly_list': monthly_list})

def ew_add(request):
    if request.method == 'POST':
        # person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        month = request.POST.get('billreceipt-month')
        year = request.POST.get('billreceipt-year')
        if not new_persons.name.endswith('.csv'):
            messages.error(request, 'wrong format')
            return render(request, 'EW/ew_add.html')

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        for data in imported_data:
            
        	value = MonthlyEW(
        		data[0],
        		data[1],
        		 data[2],
        		 data[3],
                 data[4],
                 data[5],
                 data[6],
                 month,
                 year
        		)
        	value.save()
            
    return render(request, 'EW/ew_add.html')

def ew_month(request, year, month):

    monthly_list = MonthlyEW.objects.filter(year = year).filter(month = month)

    return render(request, 'EW/ew_month.html', {'monthly_list': monthly_list})

