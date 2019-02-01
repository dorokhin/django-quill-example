from django.forms import ModelForm, HiddenInput, TextInput
from .models import Article


class ArticleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'test', 'placeholder': 'Article Title'})

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
        ]
        widgets = {'content': HiddenInput()}

