from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm


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
            return render(request, 'items/success.html', {'item': item})
    else:
        form = ItemForm()

    return render(request, 'items/add_item.html', {
        'form': form
    })

