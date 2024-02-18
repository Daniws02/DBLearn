from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.

def list_product(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'list_product.html' ,context)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_product')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'create_product.html', context)

def detail_product(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(request, 'detail_product.html', context)

def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_product')
    else:
        form = ProductForm(instance=product)
    context = {
        'form': form
    }
    return render(request, 'update_product.html', context)

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('list_product')
    context = {
        'product' : product
    }
    return render(request, 'delete_product.html', context)
