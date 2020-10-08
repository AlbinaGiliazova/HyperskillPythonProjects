from django.urls import path, re_path
from news.views import NewsView, NewsListView, NewsCreateView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    re_path("(?P<link>[^/]*)/?", NewsView.as_view(), name='news'),
]
