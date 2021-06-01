from django import forms
from django.shortcuts import redirect, render
from .forms import RequestPost, UpdateRoomService
from .models import RoomService    
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.
def room_services(request):
    if request.user.userprofile.is_owner:
        services = RoomService.objects.all().order_by('-created_at')
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

# Update a specific room
def room_service_update(request, pk):
    room_service = RoomService.objects.get(id = pk)
    form = UpdateRoomService(instance = room_service)
    if request.method == 'POST':
        form = UpdateRoomService(request.POST, instance = room_service)
        if form.is_valid:
            form.save()
            messages.success(request, "Request is updated successfully")
            return redirect('room_services')

    context = {'form': form}
    
    return render(request, 'roomservices/O-roomservice-update.html', context)