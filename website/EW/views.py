from django.shortcuts import render

# Create your views here.
def ew(request):
    return render(request, 'EW/ew.html')

def ew_add(request):
    return render(request, 'EW/ew_add.html')

def ew_month(request):
    return render(request, 'EW/ew_month.html')