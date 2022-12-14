from django.db import models

class StatusCrm(models.Model):
    Status_name =models.CharField(max_length=100, verbose_name='Статус')

    def __str__(self):
        return self.Status_name
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name = 'Дата регистрации')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Тел-номер')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'
    
class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Заявка' )
    comment_text = models.TextField(verbose_name='Текст коментарии')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.comment_text
    
    class Meta:
        verbose_name = 'Коментария'
        verbose_name_plural = 'Коментарии'
    
