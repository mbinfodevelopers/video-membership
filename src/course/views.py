from django.shortcuts import render, get_object_or_404
from .models import Category, Course


def all_courses(request):
    course = Course.objects.all()
    context = {
        'course': course
    }
    return render(request, 'shared/content.html', context)