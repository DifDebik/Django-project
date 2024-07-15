from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404

from .models import Article

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,

)
# Create your views here.


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, id=id_)
