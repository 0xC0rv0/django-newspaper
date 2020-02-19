from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    )

urlpatterns = [
    path('',ArticleListView.as_view(), name='article_list'),
]
