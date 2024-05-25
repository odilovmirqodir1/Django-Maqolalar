from django.contrib import admin
from .models import Category, NewsModel


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_editable = ('category',)
