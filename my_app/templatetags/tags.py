from my_app.models import *
from django import template

register = template.Library()


@register.simple_tag()
def get_all_categories():
    categories = Category.objects.all()
    return categories


@register.simple_tag()
def category_by_articles_jahon():
    category = Category.objects.get(pk=2)
    articles = NewsModel.objects.filter(category=category).order_by('created_at')
    return articles


@register.simple_tag()
def category_by_articles_sport():
    category = Category.objects.get(pk=3)
    articles = NewsModel.objects.filter(category=category).order_by('created_at')
    return articles
