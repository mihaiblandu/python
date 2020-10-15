from django.shortcuts import render
from .form import ProductForm
# Create your views here.
from products.models import Product

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title' : obj.title,
        'description' : obj.description
    }
    return render(request,"product/details.html", context)
def product_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title' : obj.title,
        'description' : obj.description
    }
    return render(request,"details.html", context)

def product_list(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products_list.html", context)
