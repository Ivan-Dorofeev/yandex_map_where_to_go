# Generated by Django 4.1.6 on 2023-02-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_remove_image_позиция_image_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='index',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Позиция'),
        ),
    ]
