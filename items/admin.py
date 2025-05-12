from django.contrib import admin
from .models import Category, Item

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'category', 'condition', 'created_at')

