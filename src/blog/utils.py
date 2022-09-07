from django.db.models import Q
from .models import Article
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


def paginatorArticles(request, articles, results):
    page = request.GET.get('page')
    paginator = Paginator(articles, results)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        articles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        articles = paginator.page(page)

    leftIndex = (int(page) - 1)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, articles


def article_search(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    article = Article.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query),
        status='p'
    )
    return article, search_query