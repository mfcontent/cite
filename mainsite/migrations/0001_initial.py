# Generated by Django 4.1.7 on 2023-04-04 13:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='For_me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='image/For_me/25', verbose_name='Обложка')),
                ('text', models.TextField(blank=True, verbose_name='Описание')),
                ('avail', models.BooleanField(default=True, verbose_name='Активость')),
            ],
            options={
                'verbose_name': 'Обо мне',
                'verbose_name_plural': 'Обо мне',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Nevs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Имя')),
                ('date', models.DateField(blank=True, default=datetime.date(2023, 4, 4), verbose_name='Дата создания')),
                ('logo', models.ImageField(blank=True, upload_to='image/Nevs/4204', verbose_name='Обложка')),
                ('description', models.TextField(blank=True, verbose_name='Тизер новости')),
                ('main_text', models.TextField(blank=True, verbose_name='Тело новости')),
                ('available', models.BooleanField(default=True, verbose_name='Активость')),
            ],
            options={
                'verbose_name': 'Новсть',
                'verbose_name_plural': 'Новости',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='image/Partners/81', verbose_name='Обложка')),
                ('avail', models.BooleanField(default=True, verbose_name='Активость')),
            ],
            options={
                'verbose_name': 'Партнеры',
                'verbose_name_plural': 'Партнеры',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Назвение услуги')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Zaiavki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Имя')),
                ('date', models.DateField(blank=True, default=datetime.date(2023, 4, 4), verbose_name='Дата создания')),
                ('svaz', models.CharField(blank=True, max_length=200, verbose_name='Способ связи')),
                ('description', models.TextField(blank=True, verbose_name='Описание заказа')),
                ('status', models.TextField(blank=True, verbose_name='Стастус заявки')),
                ('available', models.BooleanField(default=True, verbose_name='Активость')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название кейса')),
                ('slug', models.SlugField(max_length=200, verbose_name='Уникальный url (Генерируется сам)')),
                ('logo', models.ImageField(blank=True, upload_to='image/Keys/38', verbose_name='Обложка')),
                ('description', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('text', models.TextField(blank=True, verbose_name='Полное описание')),
                ('available', models.BooleanField(default=True, verbose_name='Активость')),
                ('services', models.ManyToManyField(to='mainsite.services', verbose_name='Услуги')),
            ],
            options={
                'verbose_name': 'Кейсы',
                'verbose_name_plural': 'Кейсы',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='image/Keys/5142', verbose_name='Фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mainsite.keys')),
            ],
            options={
                'verbose_name': 'Дополнительное фото',
                'verbose_name_plural': 'Дополнительные фото',
            },
        ),
    ]
