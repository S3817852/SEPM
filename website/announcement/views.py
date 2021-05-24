from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddAnnouncementForm
from django.contrib.auth.decorators import login_required
from .models import Announcement
from django.views import View
from django.contrib.auth.models import User
from userprofile.models import ConversationMessage
from notification.utilities import create_notification

# Create your views here.
# Announcement URL
def index(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    if request.user.userprofile.is_owner:
        return render(request, 'announcement/O-announcement.html', {'announcements': announcements} )
    else:
        return render(request, 'announcement/T_announcement.html', {'announcements': announcements} )

# Get specific announcement
class AnnouncementObjectMixin(object):
    model = Announcement
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj

# Get specific user
class UserObjectMixin(object):
    model_user = User
    def get_user(self, user_id):
        # id = self.kwargs.filter(id='id')
        user = None
        if user_id is not None:
            user = get_object_or_404(self.model_user, username=user_id)
        return user

@login_required
def add_announcement(request):
    # sent_to_tenant = Userprofile.objects.all()
    if request.method == 'POST':
        form = AddAnnouncementForm(request.POST)

        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.created_by = request.user
            announcement.save()
            # for tenant in sent_to_tenant:
            #     if not tenant.is_owner:
            #         create_notification(request, tenant.user, 'application', extra_id=job.id)
            
            return redirect('index')
    else:
        form = AddAnnouncementForm()
    
    return render(request, 'announcement/O-announcementadd.html', {'form': form})

# View detail of announcement
class AnnouncementDetailView(AnnouncementObjectMixin,UserObjectMixin,View):
    template_name = 'announcement/O-announcementdetail.html'
    template_name1 = 'announcement/T-announcementdetail.html'
    def get(self, request, id = None, *args, **kwargs):
        context = {'announcement': self.get_object()}
        if request.user.userprofile.is_owner:
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name1, context)

    def post(self, request,id =None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['announcement'] =  obj
            # form = CourseModelForm(request.POST, instance=obj)
            if request.method == 'POST':
                content = request.POST.get('content')
                # Choose

                # Choose receiver !!!
                # to_user = request.POST.get('to')
                # sent_to_user = self.get_user(to_user)
                # print(sent_to_user)
                print(obj.created_by)
                print(request.user.username)
                
                if content:
                    conversationmessage = ConversationMessage.objects.create(announcement=obj, content=content, created_by=request.user)
                    if str(obj.created_by) != str(request.user.username):
                        create_notification(request,obj.created_by , 'message', extra_id=obj.id)

                    return redirect('announcement_detail', id=obj.id)
            # if form.is_valid():
            #     form.save()
            
            # context['form'] =  form
        if request.user.userprofile.is_owner:
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name1, context)