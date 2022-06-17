from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from services.models import Announcement

from .models import Notification


@login_required
def notifications(request):
    # if Notification.created_by != Notification.to_user:
        goto = request.GET.get('goto', '')
        notification_id = request.GET.get('notification', 1)
        extra_id = request.GET.get('extra_id', 0)
        
        if goto != '':
            notification = Notification.objects.get(pk=notification_id)
            notification.is_read = True
            notification.save()
            

            if notification.notification_type == Notification.ANNOUNCEMENT:
                return redirect('announcement_detail', id=notification.extra_id)
            # elif notification.notification_type == Notification.APPLICATION:
            #     return redirect('announcement_detail', job=notification.extra_id)
            elif notification.notification_type == Notification.COMMENT:
                return redirect('announcement_detail', job_id=notification.extra_id)



    
   
        if request.user.account.is_owner:
            return render(request, 'social/O-notifications.html')
        else:
            return render(request, 'notification/T-notifications.html')
