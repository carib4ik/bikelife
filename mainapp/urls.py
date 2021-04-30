from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', ArticlesByCategory.as_view(), name='category'),
    path('article/<str:slug>/', GetArticle.as_view(), name='article'),
    path('search/', Search.as_view(), name='search'),
]