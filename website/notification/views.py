from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Notification
from announcement.models import Announcement

@login_required
def notifications(request):
    # if Notification.created_by != Notification.to_user:
        goto = request.GET.get('goto', '')
        notification_id = request.GET.get('notification', 1)
        extra_id = request.GET.get('extra_id', 0)
        announcement = Announcement.objects.all()
        if goto != '':
            notification = Notification.objects.get(pk=notification_id)
            notification.is_read = True
            notification.save()
            

            if notification.notification_type == Notification.MESSAGE:
                return redirect('announcement_detail', id=notification.extra_id)
            # elif notification.notification_type == Notification.APPLICATION:
            #     return redirect('announcement_detail', job=notification.extra_id)
            elif notification.notification_type == Notification.COMMENT:
                return redirect('announcement_detail', job_id=notification.extra_id)

        context = {'announcement_list': announcement}

    
   
        if request.user.userprofile.is_owner:
            return render(request, 'notification/O-notifications.html', context)
        else:
            return render(request, 'notification/T-notifications.html', context)
