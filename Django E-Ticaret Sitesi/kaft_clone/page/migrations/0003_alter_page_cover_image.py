# Generated by Django 3.2.9 on 2024-07-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='page'),
        ),
    ]
