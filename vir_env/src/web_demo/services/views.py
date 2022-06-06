from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from .models import MonthlyEW, Announcement
from .filter import AnnouncementFilter
from .forms import AddAnnouncementForm
from tablib import Dataset


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

def ew_month(request, year, month):

    monthly_list = MonthlyEW.objects.filter(year = year).filter(month = month)
    for bill in monthly_list:
        electricity_monthly = bill.electricity_consumption * bill.electricity_cost
        water_monthly = bill.water_consumption * bill.water_cost
        # print(bill.account.id)
        # print("elec " + str(electricity_monthly))
        # print("water " + str(water_monthly))


    return render(request, 'EW/ew_month.html', {'monthly_list': monthly_list})

def ew_add(request):
    if request.method == 'POST':
        # person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        month = request.POST.get('billreceipt-month')
        year = request.POST.get('billreceipt-year')
        if not new_persons.name.endswith('.csv'):
            messages.error(request, 'wrong format')
            return render(request, 'EW/ew_add.html')

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        for data in imported_data:
            
        	value = MonthlyEW(
        		data[0],
        		data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                month,
                year
        		)
        	value.save()
        messages.success(request,"New monthyly electricity and water data is created successfully")
        return redirect('ew')
            
    return render(request, 'EW/ew_add.html')





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
                
                # if content:
                #     conversationmessage = ConversationMessage.objects.create(announcement=obj, content=content, created_by=request.user)
                #     if str(obj.created_by) != str(request.user.username):
                #         create_notification(request,obj.created_by , 'message', extra_id=obj.id)

                return redirect('announcement_detail', id=obj.id)
            # if form.is_valid():
            #     form.save()
            
            # context['form'] =  form
        if request.user.userprofile.is_owner:
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name1, context)

@login_required
def add_announcement(request):
    # sent_to_tenant = Userprofile.objects.all()
    if request.method == 'POST':
        form = AddAnnouncementForm(request.POST)

        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.created_by = request.user.userprofile
            announcement.save()
            # for tenant in sent_to_tenant:
            #     if not tenant.is_owner:
            #         create_notification(request, tenant.user, 'application', extra_id=job.id)
            
            return redirect('announcement')
    else:
        form = AddAnnouncementForm()
    
    return render(request, 'announcement/O-announcementadd.html', {'form': form})