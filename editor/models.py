import os
import uuid
import bleach
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    # This should touch before saving
    def save(self, *args, **kwargs):
        tags = [
            'b',
            'p',
            'u',
            'h1',
            'h2',
            'em',
            'br',
            'pre',
            'strong',
        ]
        attrs = {
            '*': ['class'],
            'a': ['href', 'rel'],
            'img': ['alt', 'width', 'height', 'src'],
        }
        print(self.content)
        self.content = bleach.clean(self.content,
                                    tags=tags,
                                    attributes=attrs,
                                    )
        print(self.content)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('editor:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


def get_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{0}.{1}".format(uuid.uuid4(), ext)
    return os.path.join('img/blog/', filename)


class Image(models.Model):
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE, blank=True, null=True)
    file = models.ImageField(upload_to=get_file_name, verbose_name='Image')
    uploaded_at = models.DateTimeField(auto_now_add=True)
