# Generated by Django 3.2.9 on 2024-07-19 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20240719_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]