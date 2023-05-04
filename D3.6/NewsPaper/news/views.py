from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    ordering = '-datetime_post'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class NewDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class NewsSearch(ListView):
    model = Post
    ordering = '-datetime_post'
    template_name = 'search.html'
    context_object_name = 'news_search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
