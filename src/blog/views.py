from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from .utils import paginatorArticles, article_Search

# Get All Blogs WithOut Category
def all_blog(request):
    the_articles, search_query = article_Search(request)
    custom_range, the_articles = paginatorArticles(request, the_articles, 2)
    context = {
        "count_article": Article.objects.filter(status='p').count(),
        "the_articles": the_articles,
        "custom_range": custom_range,
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
        "article": get_object_or_404(Article, slug=slug, status='p')
    }
    return render(request, 'blog/detail_blogs.html', context)
