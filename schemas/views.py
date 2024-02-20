from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm

# Create your views here.

def list(request, model_name):
    model = globals()[model_name]
    objects = model.objects.all()
    return render(request, 'object_list.html', {'objects': objects, 'model_name': model_name})

def detail(request, model_name, id):
    model = globals()[model_name]
    object = get_object_or_404(model, id=id)
    return render(request, 'object_detail.html', {'object': object, 'model_name': model_name})

def create(request, model_name):
    model = globals()[model_name]
    form_class = globals()[f'{model_name}Form']
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list', model_name=model_name)
    else:
        form = form_class()
    return render(request, 'object_form.html', {'form': form, 'model_name': model_name})

def update(request, model_name, id):
    model = globals()[model_name]
    object = get_object_or_404(model, id=id)
    form_class = globals()[f'{model_name}Form']
    if request.method == 'POST':
        form = form_class(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('list', model_name=model_name)
    else:
        form = form_class(instance=object)
    return render(request, 'object_form.html', {'form': form, 'model_name': model_name, 'update': True})

def delete(request, model_name, id):
    model = globals()[model_name]
    object = get_object_or_404(model, id=id)
    object.delete()
    return redirect('list', model_name=model_name)