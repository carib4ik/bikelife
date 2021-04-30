from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import F


class Home(ListView):
    model = Category
    template_name = 'mainapp/index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'bike something'
        return context


class ArticlesByCategory(ListView):
    template_name = 'mainapp/articles_list.html'
    context_object_name = 'articles'
    allow_empty = False

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class GetArticle(DetailView):
    model = Article
    template_name = 'mainapp/single.html'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Article.objects.get(slug=self.kwargs['slug'])
        return context


class Search(ListView):
    template_name = 'mainapp/search.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context


