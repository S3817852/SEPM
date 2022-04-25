from django.shortcuts import render
from .models import MonthlyEW, Announcement
from .filter import AnnouncementFilter

# Create your views here.
def ew(request):
    monthly_List = MonthlyEW.objects.all()   # Get all record in data
    count = monthly_List.count()

    year_list = []
    month_list = []
    unique_id_list = []
    for obj in monthly_List:
        if obj.year not in year_list:
            year_list.append(obj.year)
        if obj.month not in month_list:
            month_list.append(obj.month)
            unique_id_list.append(obj.id)

    # for i in unique_id_list:
    #     print(i)

    monthly_list = MonthlyEW.objects.filter(pk__in = unique_id_list).order_by("-year")
    return render(request, 'EW/ew.html',{'monthly_list': monthly_list, 'count': count})

def is_valid_queryparam(param):
    return param != '' and param is not None

def announcement(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    options = request.GET.get('announcementmenu')
    if is_valid_queryparam(options) and options != 'None':
        announcements = announcements.filter(is_read = options)
    announcement_filter = AnnouncementFilter(request.GET, queryset= announcements)
    announcements = announcement_filter.qs
    if request.user.userprofile.is_owner:
        return render(request, 'announcement/O-announcement.html', {'announcements': announcements, 'filter':announcement_filter} )
    else:
        return render(request, 'announcement/T_announcement.html', {'announcements': announcements} )