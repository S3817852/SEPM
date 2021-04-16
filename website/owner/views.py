from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .form import ProductForm, RawProductForm

def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            #now the data is good
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors )
    context = {
        "form": my_form
    }
    return render(request,"product/product_create.html",context )


# def product_create_view(request):
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     context = {
        
#     }
#     return render(request,"product/product_create.html",context )


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request,"product/product_create.html",context )

def product_details_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request,"product/product_details.html",context )