from django.urls import path
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from .models import Article
from .views import AddArticleFormView, ArticleListView, ArticleDetailView, ArticleUpdate, ImageUploadView

app_name = 'editor'

info_dict = {
    'queryset': Article.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = [
    path('sitemap.xml', sitemap,
         {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),
    path('add', AddArticleFormView.as_view(), name='add'),
    path('', ArticleListView.as_view(), name='list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', ArticleUpdate.as_view(), name='edit'),
    path('upload-image/', ImageUploadView.as_view(), name='upload_image')
]
