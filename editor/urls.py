from django.urls import path
from .views import AddArticleFormView, ArticleListView, ArticleDetailView, ArticleUpdate

app_name = 'editor'

urlpatterns = [
    path('add', AddArticleFormView.as_view(), name='add'),
    path('', ArticleListView.as_view(), name='list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', ArticleUpdate.as_view(), name='edit'),
]
