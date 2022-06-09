from django.shortcuts import render

# Create your views here.
def dong_lun(request):
    dong = 'vip_pro'
    return render(request, 'donglun.html', {'dong_name': dong})