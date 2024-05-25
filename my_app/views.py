from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import NewsModel, Category


def index(request):
    articles = NewsModel.objects.filter(is_published=True).order_by('created_at')
    context = {
        'articles': articles,
        'title': "Bosh sahifa"
    }
    return render(request, 'index.html', context)


def get_categories_id(request, pk):
    category = get_object_or_404(Category, pk=pk)
    articles_by_categories = NewsModel.objects.filter(category=category)
    context = {
        'articles_by_categories': articles_by_categories,
        'title': category.title
    }
    return render(request, 'category_detail.html', context)


def post_detail(request, pk):
    article_detail = get_object_or_404(NewsModel, pk=pk)
    context = {
        "article_detail": article_detail,
        "title": article_detail.title
    }
    return render(request, "post_detail.html", context)


