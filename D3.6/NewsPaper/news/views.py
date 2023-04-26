from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-datetime_post'
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

class NewDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
