from django.shortcuts import render

# Create your views here.

# Bills view
def room_consumption_view(request):
    return render(request, 'bills/roomconsumption.html', {})