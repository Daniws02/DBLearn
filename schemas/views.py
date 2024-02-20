from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm

# Create your views here.

def list(request, model_name):
    model_class = get_model(model_name)
    objects = model_class.objects.all()
    return render(request, 'object_list.html', {'objects': objects, 'model_name': model_name})

def detail(request, model_name, id):
    model_class = get_model(model_name)
    object = get_object_or_404(model_class, id=id)
    return render(request, 'object_detail.html', {'object': object, 'model_name': model_name})

def create(request, model_name):
    model_class = get_model(model_name)
    form_class = get_form(model_name)
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list', model_name=model_name)
    else:
        form = form_class()
    return render(request, 'object_form.html', {'form': form, 'model_name': model_name})

def update(request, model_name, id):
    model_class = get_model(model_name)
    object = get_object_or_404(model_class, id=id)
    form_class = get_form(model_name)
    if request.method == 'POST':
        form = form_class(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('list', model_name=model_name)
    else:
        form = form_class(instance=object)
    return render(request, 'object_form.html', {'form': form, 'model_name': model_name, 'update': True})

def delete(request, model_name, id):
    model_class = get_model(model_name)
    object = get_object_or_404(model_class, id=id)
    object.delete()
    return redirect('list', model_name=model_name)

def get_model(model_name):
    if model_name == 'product':
        return Product
    elif model_name == 'category':
        return Category
    # Adicione mais modelos conforme necessário

def get_form(model_name):
    if model_name == 'product':
        return ProductForm
    elif model_name == 'category':
        return CategoryForm
    # Adicione mais formulários conforme necessário