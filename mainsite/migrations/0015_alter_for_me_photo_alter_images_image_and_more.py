# Generated by Django 4.1.7 on 2023-04-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0014_alter_for_me_photo_alter_images_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='for_me',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image/For_me/34', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/Keys/7187', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='keys',
            name='logo',
            field=models.ImageField(blank=True, upload_to='image/Keys/5789', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='nevs',
            name='date',
            field=models.DateField(blank=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='nevs',
            name='logo',
            field=models.ImageField(blank=True, upload_to='image/Nevs/5674', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image/Partners/74', verbose_name='Обложка'),
        ),
    ]
