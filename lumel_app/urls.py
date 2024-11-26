from django.urls import path
from .views import MainView, ArticleListView, ArticleDetailView, LegalsView

app_name = 'lumel_app'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path("actualites/", ArticleListView.as_view(), name='actualites'),
    path("actualites/<int:pk>", ArticleDetailView.as_view(), name='detail-actualite'),
    path("legals/", LegalsView.as_view(), name='legals'),
]
