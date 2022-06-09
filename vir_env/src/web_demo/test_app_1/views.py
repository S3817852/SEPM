from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def tuan_page(request):
    abc = 'string'
    return render( request, "tuan_page.html", {'abc_variable':abc})