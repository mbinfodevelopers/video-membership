# Generated by Django 4.0.6 on 2022-08-01 14:53

import course.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_teacher_alter_comment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=course.models.get_video_filepath),
        ),
    ]