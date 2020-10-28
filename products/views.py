from django.shortcuts import render,get_object_or_404 ,redirect
from .form import ProductForm
from django.http import Http404
# Create your views here.
from .models import Product

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        # now data is good
        print(form.cleaned_data)
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "product_delete.html", context)
def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('.')
    context = {
        'form': form
    }
    return render(request, "product_update.html", context)
def product_detail_view(request, id):
    try:
        obj = get_object_or_404(Product, id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "obj": obj
    }
    return render(request, "details.html", context)

def product_view(request):
    return render(request,"product/product.html", {})

def product_list(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products_list.html", context)
