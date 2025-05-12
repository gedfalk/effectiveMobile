from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm


@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('index')
    else:
        form = ItemForm()

    return render(request, 'items/add_item.html', {
        'form': form
    })