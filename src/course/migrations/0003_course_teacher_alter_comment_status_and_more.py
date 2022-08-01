# Generated by Django 4.0.6 on 2022-08-01 08:20

import course.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0002_comment_author_user_course_view_count_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(blank=True, choices=[('readed', 'readed'), ('unreaded', 'unreaded'), ('close', 'close')], max_length=25),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, default=course.models.get_default_course_image, null=True, upload_to=course.models.get_course_image_filepath),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(blank=True, choices=[('New Course', 'New Course'), ('Course in progress', 'Course in progress'), ('Course update', 'Course update'), ('The course is over', 'The course is over')], max_length=25),
        ),
    ]