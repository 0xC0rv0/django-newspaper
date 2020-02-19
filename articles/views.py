from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Article

class ArticleListView(ListView):
    model= Article
    template_name = 'article_list.html'
