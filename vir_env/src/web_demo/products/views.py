from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def product_view(request, *args, **kwargs):
    my_context = {
        'my_text': "This is my text",
        'my_number': 123
    }
    # print(request.user) 
    return render(request, "product.html", my_context)
