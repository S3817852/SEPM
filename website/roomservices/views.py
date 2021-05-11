from django.shortcuts import render

# Create your views here.
def room_services(request):
    return render(request, 'roomservices/O-roomservice.html')

def room_services_details(request):
    return render(request, 'roomservices/O-roomservicedetail.html')