from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

from django.shortcuts import render
from .models import Item

def home(request):
    items = Item.objects.all()  # Fetch all items
    return render(request, 'inventory/home.html', {'items': items})


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = ItemForm()
    return render(request, 'inventory/add_item.html', {'form': form})

def edit_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/edit_item.html', {'form': form})

def delete_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'inventory/delete_item.html', {'item': item})
