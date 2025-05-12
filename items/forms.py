from django import forms
from .models import Item, Category


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'image', 'category', 'condition']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите название товара'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Введите описание товара...',
                'rows': 3,
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
            'condition': forms.Select(attrs={
                'class': 'form-select',
            }),
            'image': forms.FileInput(),

        }