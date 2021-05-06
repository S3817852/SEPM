from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# from job.models import Job
from userprofile.models import Userprofile

@login_required
def frontpage(request):
    # jobs = Job.objects.filter(status=Job.ACTIVE).order_by('-created_at')[0:3]
    if request.user.userprofile.is_owner:
        return render(request, 'core/ownermain.html',{})
    else:
        return render(request, 'core/tenantmain.html',{})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'owner')

            if account_type == 'owner':
                userprofile = Userprofile.objects.create(user=user, is_owner=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()

            login(request, user)

            return redirect('fontpage')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})