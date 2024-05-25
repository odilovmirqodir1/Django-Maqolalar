from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:pk>/', views.get_categories_id, name='category'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
]
