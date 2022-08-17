from django.urls import path
from course.api.views import course_video_list


urlpatterns = [
    path('video_list/<slug:category_slug>/<slug:course_slug>/', course_video_list, name='video_list')
]