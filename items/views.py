from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item, Category
from .forms import ItemForm


def catalogue(request, category_id=None):
    items = Item.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        items = items.filter(category=category)

    context = {
        'items': items,
        'categories': categories,
        'current_category': category_id
    }
    return render(request, 'items/catalogue.html', context)

def search(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'items/search.html', context)

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    is_owner = request.user == item.user
    return render(request, 'items/item_detail.html', {
        'item': item,
        'is_owner': is_owner
    })

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            # return redirect('index')
            return render(request, 'items/success.html', {
                'item': item,
                'action': 'added'
                }
            )
    else:
        form = ItemForm()

    return render(request, 'items/add_item.html', {
        'form': form
    })

@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, user=request.user)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            # return redirect('item_detail', pk=item.pk)
            return render(request, 'items/success.html', {
                'item': item,
                'action': 'edited'
                }
            )
    else:
        form = ItemForm(instance=item)
    
    return render(request, 'items/edit_item.html', {
        'form': form,
        'item': item
    })

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'items/confirm_delete.html', {'item': item})

