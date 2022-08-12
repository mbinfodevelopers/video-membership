from django.shortcuts import render, get_object_or_404,HttpResponse
from home.models import Category
from .models import Course


def all_courses(request, category_slug=None):
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(category=categories, is_active=True)
        course_count = Course.objects.filter(category=categories).count()
    else:
        courses = Course.objects.all().filter(is_active=True)
        course_count = Course.objects.count()
    context = {
        'courses': courses,
        'course_count': course_count
    }

    return render(request, 'course/all_courses.html', context)


def course_detail(request, category_slug, course_slug):
    try:
        single_course = Course.objects.get(category__slug=category_slug, slug=course_slug)
    except Exception as e:
        raise e
    context = {
        'single_course': single_course
    }

    return render(request, 'course/course_detail.html', context)