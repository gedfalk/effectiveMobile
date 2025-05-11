from django.shortcuts import render
from items.models import Item

def index(request):
    items = Item.objects.select_related('user_id', 'category').all().order_by('created_at')
    context = {'items': items}
    return render(request, 'main/index.html', context)
