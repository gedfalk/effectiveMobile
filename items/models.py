from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    item_condition = [
        ('new', 'Новый'), 
        ('used', 'б/у'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=100, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    # image_url
    image = models.ImageField(upload_to='item_images', blank=True, null=True) 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    condition = models.CharField(max_length=20, choices=item_condition, verbose_name='Состояние')
    # item_id... он ведь должен создавать автоматически?.. или я путаю? 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Товар'