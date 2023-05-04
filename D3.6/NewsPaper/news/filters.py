import django_filters
from django.forms import DateInput
from django_filters import FilterSet

from .models import Post, Category


class PostFilter(FilterSet):
    model = Post
    fields = {'title', 'category', 'datetime_post'}
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Title',
    )
    date = django_filters.DateFilter(
        field_name='datetime_post',
        lookup_expr='gt',
        label='Date',
        widget=DateInput(
            attrs={'type': 'date'},
        ),
    )
    category = django_filters.ModelChoiceFilter(
        field_name='categories',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='Любая',
    )
