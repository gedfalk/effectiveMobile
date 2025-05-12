from django.shortcuts import render
from items.models import Item
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.models import User

def index(request):
    items = Item.objects.select_related('user', 'category').all().order_by('created_at')
    context = {'items': items}
    return render(request, 'main/index.html', context)

def user_selection(request):
    return render(request, 'main/user_selection.html', {
        'available_users': User.objects.all()
    })

def switch_user(request, user):
    user = User.objects.get(id=user)
    login(request, user)
    return redirect('index')