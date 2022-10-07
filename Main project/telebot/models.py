from tabnanny import verbose
from django.db import models

class Tele_Settings(models.Model):
    tele_token = models.CharField(max_length=100, verbose_name='Токен бота')
    tele_chat_id = models.CharField(max_length=20, verbose_name='Чат айди бота' )
    tele_text = models.TextField(verbose_name='Текст бота')

    def __str__(self):
        return self.tele_chat_id

    class Meta:
        verbose_name = 'Настройка бота'
        verbose_name_plural = 'Настройки'
