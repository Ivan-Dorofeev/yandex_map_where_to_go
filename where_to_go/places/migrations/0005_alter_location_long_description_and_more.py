# Generated by Django 4.1.6 on 2023-02-12 09:07

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_rename_description_location_long_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='long_description',
            field=models.CharField(blank=True, max_length=500, verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='location',
            name='short_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
    ]
