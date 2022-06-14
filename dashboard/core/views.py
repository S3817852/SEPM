from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'base_page.html', {})

def dashborad(request):
    return render(request, 'dashboard.html', {})

def ew(request):
    return render(request, 'ew.html', {})
