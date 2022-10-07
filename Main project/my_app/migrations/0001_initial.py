# Generated by Django 4.1.1 on 2022-09-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_dt', models.DateField(auto_now=True)),
                ('order_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('order_phone', models.CharField(max_length=200, verbose_name='Тел-номер')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]