# Generated by Django 4.0.6 on 2022-09-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='position',
            field=models.IntegerField(verbose_name='پوزیشن'),
        ),
    ]