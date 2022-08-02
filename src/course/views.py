from django.shortcuts import render, get_object_or_404
from .models import Category, Course


def all_courses(request):
    courses = Course.objects.filter(is_active=True).order_by('-create_date')
    context = {
        'courses': courses
    }
    return render(request, 'course/courses.html', context)