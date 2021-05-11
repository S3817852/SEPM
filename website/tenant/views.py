from django.shortcuts import render

# Create your views here.
def tenant(request):
    return render(request, 'tenant/tenant.html')