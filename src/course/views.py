from django.shortcuts import render

def index_homepage(request):

    return render(request, 'course/index.html')