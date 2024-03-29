# Generated by Django 4.0.6 on 2023-03-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=55, unique=True, verbose_name='دسته بندی کلی ')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name=' آدرس اسلاگ ')),
                ('description', models.TextField(blank=True, max_length=255, verbose_name='توضیحات ')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی کلی',
            },
        ),
    ]
