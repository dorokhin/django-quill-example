# Generated by Django 2.1.5 on 2019-02-03 04:23

from django.db import migrations, models
import django.db.models.deletion
import editor.models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0002_article_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to=editor.models.get_file_name, verbose_name='Image')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='editor.Article')),
            ],
        ),
    ]
