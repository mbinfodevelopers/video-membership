from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from course.models import Course, Video
from course.api.serializers import CourseVideoSerializer


@api_view(['GET'])
def course_video_list(request, category_slug, course_slug):
    if request.method == 'GET':
        single_course = Course.objects.get(category__slug=category_slug, slug=course_slug)

        if single_course:
            videos = Video.objects.filter(course_id=single_course.id)

        serializer = CourseVideoSerializer(videos, many=True)
        return Response(serializer.data)
