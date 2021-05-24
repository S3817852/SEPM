from django import forms
from django.shortcuts import redirect, render
from .forms import RequestPost
from .models import RoomService    
from django.core.files.storage import FileSystemStorage

# Create your views here.
def room_services(request):
    if request.user.userprofile.is_owner:
        services = RoomService.objects.all()
        return render(request, 'roomservices/O-roomservice.html', {'services': services})
    else:
        services = RoomService.objects.all().order_by('-created_at')
        return render(request, 'roomservices/T-roomservice.html', {'services': services})

def room_services_details(request, id):
    if request.user.userprofile.is_owner:
        room_detail = RoomService.objects.get(id = id)
        return render(request, 'roomservices/O-roomservicedetail.html',{'room': room_detail})
    else:
        room_detail = RoomService.objects.get(id = id)
        return render(request, 'roomservices/T-roomservicedetail.html', {'room': room_detail})

def room_services_add(request):
    form = RequestPost()
    services = RoomService.objects.all()
    if not request.user.userprofile.is_owner:
        
        if request.method == 'POST':

            form = RequestPost(request.POST, request.FILES)
            if form.is_valid():
                new_service = form.save(commit=False)
                new_service.created_by = request.user
                new_service.save()
                return redirect('room_services')
            # upload_file = request.FILES['image']
            # fs = FileSystemStorage()
            # fs.save(upload_file.name, upload_file)
        context = {'form': form}
        return render(request, 'roomservices/T-roomserviceadd.html',context)