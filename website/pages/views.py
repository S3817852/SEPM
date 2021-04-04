from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    my_context = {
        "title": "this is about us",
        "my_number": 123,
        "my_list": [11, 23, 38, "abc"],
        "my_html_text":"<h1>Good Morning</h1>"
    }
    # return HttpResponse("Hello World")
    return render(request, "home.html", my_context)

def contact_view(request):
    return render(request, "contact.html",{})
    # return HttpResponse("Contact page")