from django.shortcuts import render

# Create your views here.
def room_services(request):
    if request.user.userprofile.is_owner:
        return render(request, 'roomservices/O-roomservice.html')
    else:
        return render(request, 'roomservices/T-roomservice.html')

def room_services_details(request):
    return render(request, 'roomservices/O-roomservicedetail.html')