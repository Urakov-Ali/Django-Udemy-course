from tabnanny import verbose
from django.db import models

class PriceCard(models.Model):
    pc_description = models.CharField(max_length=100, verbose_name='Тайтл прайса')
    pc_value = models.CharField(max_length=20, verbose_name='Цены')

    def __str__(self):
        return self.pc_value
    
    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

class PriceTable(models.Model):
    pt_title = models.CharField(max_length=100, verbose_name='Услуга')
    pt_old_price  = models.CharField(max_length=50, verbose_name='Старая цена')
    pt_new_price = models.CharField(max_length=20, verbose_name='Новая цена')

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'