# Generated by Django 4.1 on 2022-09-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_order_order_status_commentcrm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_dt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
