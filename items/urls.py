from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('add/', views.add_item, name='add_item'),
]
