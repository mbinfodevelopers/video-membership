from rest_framework import serializers
from course.models import Video, Course


class CourseVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'video', 'id']