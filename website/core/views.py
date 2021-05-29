from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# from job.models import Job
from userprofile.models import Userprofile
from userprofile.forms import UserprofileUpdateForm
from .forms import CreateUserForm
from django.contrib import messages

@login_required
def frontpage(request):
    # jobs = Job.objects.filter(status=Job.ACTIVE).order_by('-created_at')[0:3]
    if request.user.userprofile.is_owner:
        return render(request, 'core/ownermain.html',{})
    else:
        
        return render(request, 'core/tenantmain.html',{})

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'owner')

            if account_type == 'owner':
                userprofile = Userprofile.objects.create(user=user, is_owner=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()

            # user = form.cleaned_data.get('username')
            messages.error(request, 'Signup successfully')

            login(request, user)

            return redirect(frontpage)
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request,
                          "core/signup.html",
                          {"form":form})
    else:
        form = CreateUserForm()


    #  {% for message in messages %}
		
	# 	{% if message.tag == 'success' %}
	# 	<p id="message">
	# 	<script>M.toast({
	# 		html: "{{message}}",
	# 		classes: "green rounded",
	# 		displayLength:2000
	# 	});</script>  </p>
	# 	{% endif %}
	# 	{% endfor %}



# {% if messages %}
# 		{%for message in messages %}
# 		{%if message.level == DEFAULT_MESSAGE_LEVELS.INFOR %}
# 		<div class="alert alert-primary" role="alert">
# 			{{message}}
# 		</div>
# 		{% elif message.level == DEFAULT_MESSAGE_LEVELS.SUCCESS %}
# 		<div class="alert alert-success" role="alert">
# 			{{message}}
# 		</div>
# 		{% elif message.level == DEFAULT_MESSAGE_LEVELS.DANGER %}
# 		<div class="alert alert-danger" role="alert">
# 			{{message}}
# 		</div>
# 		{% elif message.level == DEFAULT_MESSAGE_LEVELS.WARNING %}
# 		<div class="alert alert-warning" role="alert">
# 			{{message}}
# 		</div>
# 		{% endif %}
# 		{%endfor %}
# 		{% endif %}
    return render(request, 'core/signup.html', {'form': form})