from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

class Cms_app(models.Model):
    cms_title = models.CharField(max_length=100, verbose_name='тайтл')
    cms_text = models.TextField(verbose_name='текст')
    cms_img = models.ImageField(upload_to='sliderMedia')
    cms_css = models.CharField(max_length=100, null=True, default='-', verbose_name='css_модел')

    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
