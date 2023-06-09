from django.urls import path
from .views import NewsList, NewDetail, NewsSearch


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', NewDetail.as_view()),
   path('search', NewsSearch.as_view()),
]