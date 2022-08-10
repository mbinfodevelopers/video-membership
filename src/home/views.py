from django.shortcuts import render
from course.models import Course

def home_page(request):
    courses = Course.objects.filter(is_active=True)
    context = {
        'courses':courses
    }
    return render(request,'base/home.html',context)