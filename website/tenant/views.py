from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from userprofile.models import Userprofile

# Create your views here.
def tenant(request):
    tenant = Userprofile.objects.filter(is_owner = False)
    for instance in tenant:
        print(instance.id)
    # if( not request.user.userprofile.is_owner):
    #     print("a")
    return render(request, 'tenant/tenant.html', {'tenants': tenant})