# Generated by Django 4.1.7 on 2023-03-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertylisting',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='photo_main',
            field=models.ImageField(upload_to='photos'),
        ),
    ]