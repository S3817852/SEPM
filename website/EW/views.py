from django.shortcuts import render
from .models import MonthlyEW
from .resources import EWresources
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

# Create your views here.
def ew(request):
    return render(request, 'EW/ew.html')

def ew_add(request):
    if request.method == 'POST':
        # person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        
        
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
                 data[6]
        		)
        	value.save()
    return render(request, 'EW/ew_add.html')

def ew_month(request):
    return render(request, 'EW/ew_month.html')

