from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('add/', views.add_item, name='add_item'),
    path('<int:pk>/edit/', views.edit_item, name='edit_item'),
    path('<int:pk>/delete/', views.delete_item, name='delete_item'),
    path('catalogue/', views.catalogue, name='catalogue'),
    # path('catalogue/<int:category_id>/', views.catalogue, name='catalogue_by_category'),
    path('search', views.search, name='search'),
    
]
