from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddAnnouncementForm
from django.contrib.auth.decorators import login_required
from .models import Announcement
from django.views import View
from django.contrib.auth.models import User
from userprofile.models import ConversationMessage

# Create your views here.
def index(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcement/O-announcement.html', {'announcements': announcements} )

class AnnouncementObjectMixin(object):
    model = Announcement
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj

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

class AnnouncementDetailView(AnnouncementObjectMixin,UserObjectMixin,View):
    template_name = 'announcement/O-announcementdetail.html'
    def get(self, request, id = None, *args, **kwargs):
        context = {'announcement': self.get_object()}
        return render(request, self.template_name, context)

    def post(self, request,id =None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['job'] =  obj
            # form = CourseModelForm(request.POST, instance=obj)
            if request.method == 'POST':
                content = request.POST.get('content')
                to_user = request.POST.get('to')
                sent_to_user = self.get_user(to_user)
                print(sent_to_user)
                # queryset = User.objects.filter('to_user')
                # print(queryset)
                if content:
                    conversationmessage = ConversationMessage.objects.create(announcement=obj, content=content, created_by=request.user)
                    # create_notification(request, sent_to_user, 'message', extra_id=obj.id)

                    return redirect('announcement_detail', id=obj.id)
            # if form.is_valid():
            #     form.save()
            
            # context['form'] =  form
        return render(request, self.template_name,context)