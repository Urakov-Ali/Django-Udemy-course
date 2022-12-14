# Generated by Django 4.1.1 on 2022-09-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cms_app',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cms_title', models.CharField(max_length=100, verbose_name='тайтл')),
                ('cms_text', models.TextField(verbose_name='текст')),
                ('cms_img', models.ImageField(upload_to='sliderMedia')),
                ('cms_css', models.CharField(default='-', max_length=100, null=True, verbose_name='css_модел')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
