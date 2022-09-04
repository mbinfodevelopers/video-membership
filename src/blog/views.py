from django.shortcuts import render, get_object_or_404
from .models import Article, Category


# Get All Blogs WithOut Category
def all_blog(request):
    context = {
        "category": Category.objects.filter(status=True),
        "article": Article.objects.filter(status="p"),
        "count_article": Article.objects.filter(status='p').count()
        # "category": get_object_or_404(Category, status=True)
    }
    return render(request, 'blog/blogs.html', context)


# Gets Articles Just With Category
def category(request, slug):
    context = {
        "category": get_object_or_404(Category, slug=slug, status=True),
        "count_article": Article.objects.filter(status='p').count()
    }
    return render(request, 'blog/blogs.html', context)


# Get Article Detail
def article_detail(request, slug):
    context = {
        "article": get_object_or_404(Article, status='p', slug=slug)
    }
    return render(request, 'blog/detail_blogs.html', context)
