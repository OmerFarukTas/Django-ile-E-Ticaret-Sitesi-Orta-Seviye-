# Generated by Django 3.2.9 on 2024-07-20 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_alter_shoppingcart_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='items',
            field=models.ManyToManyField(blank=True, to='cart.ShoppingCartItem'),
        ),
    ]