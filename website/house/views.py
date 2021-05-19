from django import forms
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .forms import AddHouseForm
from .models import House, Room

# class AnnouncementDetailView(AnnouncementObjectMixin,UserObjectMixin,View):
#     template_name = 'announcement/O-announcementdetail.html'
#     template_name1 = 'announcement/T-announcementdetail.html'
#     def get(self, request, id = None, *args, **kwargs):
#         context = {'announcement': self.get_object()}
#         if request.user.userprofile.is_owner:
#             return render(request, self.template_name, context)
#         else:
#             return render(request, self.template_name1, context)

#     def post(self, request,id =None, *args, **kwargs):
#         context = {}
#         obj = self.get_object()
#         if obj is not None:
#             context['announcement'] =  obj
#             # form = CourseModelForm(request.POST, instance=obj)
#             if request.method == 'POST':
#                 content = request.POST.get('content')
#                 # Choose

#                 # Choose receiver !!!
#                 # to_user = request.POST.get('to')
#                 # sent_to_user = self.get_user(to_user)
#                 # print(sent_to_user)
#                 print(obj.created_by)
#                 print(request.user.username)
                
#                 if content:
#                     conversationmessage = ConversationMessage.objects.create(announcement=obj, content=content, created_by=request.user)
#                     if str(obj.created_by) != str(request.user.username):
#                         create_notification(request,obj.created_by , 'message', extra_id=obj.id)

#                     return redirect('announcement_detail', id=obj.id)
#             # if form.is_valid():
#             #     form.save()
            
#             # context['form'] =  form
#         if request.user.userprofile.is_owner:
#             return render(request, self.template_name, context)
#         else:
#             return render(request, self.template_name1, context)

# Create your views here.
class house(View):
    template_name = 'house/house.html'
    def get(self, request, *args, **kwargs):
        houses = House.objects.all()
        rooms = Room.objects.filter(status = 'Empty')
        rooms1 = Room.objects.filter(status = 'Rented')
        empty_room = rooms.count()
        rented_room = rooms1.count()
        context = {'empty_room': empty_room, 'houses': houses, 'rented_room': rented_room}
        if request.user.userprofile.is_owner:
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)
    
    # owners = House.objects.all()
   
    

def house_add(request):
    form = AddHouseForm()
    if request.method == 'POST':
        form = AddHouseForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'house/house_add.html', context)

def room(request):
    rooms = Room.objects.all()
    return render(request, 'house/room.html', context={'rooms': rooms})

def room_add(request):
    return render(request, 'house/room_add.html')