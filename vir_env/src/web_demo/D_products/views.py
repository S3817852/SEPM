from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }

    #return render(request, "product/detail.html", context)
    return render(request, "D_products/product_detail.html", context)

# Part 23 
# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm(request.POST or None)

#     context = {
#         'form': form
#     }

#     return render(request, "D_products/product_create.html", context)

def product_create_view(request):

    context = {}

    return render(request, "D_products/product_create.html", context)