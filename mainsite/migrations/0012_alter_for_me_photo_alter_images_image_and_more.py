# Generated by Django 4.1.7 on 2023-04-04 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0011_zaiavki_alter_for_me_photo_alter_images_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='for_me',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image/For_me/51', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/Keys/1442', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='keys',
            name='logo',
            field=models.ImageField(blank=True, upload_to='image/Keys/1674', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image/Partners/8', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='zaiavki',
            name='svaz',
            field=models.CharField(blank=True, max_length=200, verbose_name='Способ связи'),
        ),
    ]
