from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddAnnouncementForm
from django.contrib.auth.decorators import login_required
from .models import Announcement
from django.views import View

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

class AnnouncementDetailView(AnnouncementObjectMixin,View):
    template_name = 'announcement/O-announcementdetail.html'
    def get(self, request, id = None, *args, **kwargs):
        context = {'announcement': self.get_object()}
        return render(request, self.template_name, context)