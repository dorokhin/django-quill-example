import os
import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('editor:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


def get_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{0}.{1}".format(uuid.uuid4(), ext)
    return os.path.join('img/blog/', filename)


class Image(models.Model):
    post = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_name, verbose_name='Image')
