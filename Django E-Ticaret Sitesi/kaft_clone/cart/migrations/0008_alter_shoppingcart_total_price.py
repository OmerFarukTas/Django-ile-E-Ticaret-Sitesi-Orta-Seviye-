# Generated by Django 3.2.9 on 2024-07-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_alter_shoppingcart_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='total_price',
            field=models.FloatField(default=0),
        ),
    ]
