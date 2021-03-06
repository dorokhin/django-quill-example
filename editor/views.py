from .forms import ArticleForm
from django.views import View
from django.utils import timezone
from .models import Article, Image
from .forms import ImageUploadForm
from django.shortcuts import render
from django.http import JsonResponse, request
from django.core.paginator import Paginator
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


class ImageUploadView(View):

    def get(self, request):
        paginate_by = 10
        image_list = Image.objects.all()
        paginator = Paginator(image_list, paginate_by)

        page = request.GET.get('page')

        near_pages = 3
        try:
            next_pages = range(int(page) + 1, paginator.num_pages + 1)[:near_pages]
            prev_pages = set()
            page_num = int(page)
            if page_num > near_pages:
                prev_pages = set(range(page_num - 1, -paginator.num_pages, -1)[:near_pages])
                if 1 in prev_pages:
                    prev_pages.remove(1)
        except TypeError as e:
            prev_pages = None
            next_pages = None
            page_num = 1

        images = paginator.get_page(page)
        return render(self.request, 'editor/image_list.html', {
            'images': images,
            'current_page': page_num,
            'next_pages': next_pages,
            'prev_pages': prev_pages,
            'first_page': True if page_num == 1 else False,
            'last_page': True if page_num == paginator.num_pages else False,
        })

    def post(self, request):
        form = ImageUploadForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {
                'is_valid': True,
                'name': photo.file.name,
                'url': request.build_absolute_uri(photo.file.url),
            }
        else:
            data = {
                'is_valid': False,
                'errors': form.errors,
            }
        return JsonResponse(data)
