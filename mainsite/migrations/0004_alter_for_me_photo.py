# Generated by Django 4.1.7 on 2023-03-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_alter_for_me_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='for_me',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image/For_me/44', verbose_name='Обложка'),
        ),
    ]