from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Item, Category
from .forms import ItemForm
from .utils import delete_double

def search(request):
    pass

# def catalogue(request, category_id=None):
#     items = Item.objects.all().order_by('-created_at')
#     categories = Category.objects.all()

#     if category_id:
#         category = get_object_or_404(Category, id=category_id)
#         items = items.filter(category=category)

#     context = {
#         'items': items,
#         'categories': categories,
#         'current_category': category_id
#     }
#     return render(request, 'items/catalogue.html', context)

def catalogue(request):
    items = Item.objects.none()
    categories = Category.objects.all()
    conditions = Item.item_condition
    # todo: Передать в фильтр только, например, 10 самых плодовитых юзеров
    User = get_user_model()
    users = User.objects.all()

    # накидываем все фильтры в OR, и потом компануем запрос в items
    # параллельно деактивируем фильтры, если они были активированы
    filters = {}
    or_conditions = Q()
    has_any_filter = False
    if 'category' in request.GET:
        filters['category'] = request.GET.getlist('category')
        filters['category'] = delete_double(filters['category'])
        or_conditions |= Q(category_id__in=filters['category'])
        has_any_filter = True
    if 'condition' in request.GET:
        filters['condition'] = request.GET.getlist('condition')
        filters['condition'] = delete_double(filters['condition'])
        or_conditions |= Q(condition__in=filters['condition'])
        has_any_filter = True
    if 'user' in request.GET:
        filters['user'] = request.GET.getlist('user')
        filters['user'] = delete_double(filters['user'])
        or_conditions |= Q(user_id__in=filters['user'])
        has_any_filter = True

    if has_any_filter:
        items = Item.objects.filter(or_conditions)

    # Проще передать url в контексте, потому что заниматься этим в templates - это пипец
    current_url = '?'
    for filter, nums in filters.items():
        for n in nums:
            current_url += f'{filter}={n}&'
    current_url = current_url.rstrip('&')

    context = {
        'items': items,
        'categories': categories,
        'conditions': conditions,
        'users': users,
        'filters': filters,
        'current_url': current_url
    }
    return render(request, 'items/catalogue.html', context)

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

