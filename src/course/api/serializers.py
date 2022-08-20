from rest_framework import serializers
from course.models import Video, Course


class CourseVideoSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    src = serializers.CharField(source='video')

    class Meta:
        model = Video
        fields = ['title', 'src', 'id']

    def get_id(self, obj):
        new_id = f'vid_{obj.id}'
        return new_id


