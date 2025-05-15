from django.db import models
from django.contrib.auth import get_user_model
from items.models import Item

User = get_user_model()

class Trade(models.Model):
    status_choices = [
        ('accepted', 'Принята'),
        ('declined', 'Отклонена'),
        ('canceled', 'ГаляОтмена!'),
        ('inprogress', 'На рассмотрении'),
    ]

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_trades', verbose_name='Отправитель')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recieved_trades', verbose_name='Получатель')
    item_offered = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='offered', verbose_name="Предложенный товар")
    item_requested = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="requested", verbose_name="Запрошенный товар")
    comment = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=status_choices, default='inprogress')

    def __str__(self):
        return f"Предложение об обмене {self.item_offered} на {self.item_requested}"



