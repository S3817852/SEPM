from django.shortcuts import render

# Create your views here.
def account(request):
    if request.user.userprofile.is_owner:
        return render(request, "userprofile/O_account.html")
    else:
        return render(request, 'userprofile/T-account.html')

def account_update(request):
    return render(request, "userprofile/O_account_update.html")