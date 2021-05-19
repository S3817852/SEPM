from django.shortcuts import render

# Create your views here.
def account(request):
    return render(request, "userprofile/O_account.html")

def account_update(request):
    return render(request, "userprofile/O_account_update.html")