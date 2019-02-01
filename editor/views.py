from .forms import ArticleForm
from .models import Article
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView


class AddArticleFormView(CreateView):
    template_name = 'editor/add.html'
    form_class = ArticleForm
    success_url = '/'


class ArticleListView(ListView):
    model = Article
    template_name = 'editor/list.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ArticleUpdate(UpdateView):
    model = Article
    template_name_suffix = '_edit'
    form_class = ArticleForm
