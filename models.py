from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_title = models.CharField('Post_title', max_length=255)
    post_text = models.TextField('Post_text')
    post_image = models.ImageField('Post_image', null=True, blank=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.post_title


class Category(models.Model):
    name = models.CharField('Category', max_length=255)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Text')
    date = models.DateTimeField('Date', default=timezone.now)
    image = models.ImageField('Image', null=True, blank=True)
    image2 = models.ImageField('Image2', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.PROTECT, default='')
    created_at = models.DateTimeField('Date', default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField('Name', max_length=20, default='')
    comment_text = models.TextField('Comment', blank=True)
    post = models.ForeignKey(Blog, verbose_name='Blog', on_delete=models.PROTECT, blank=True)
    created_at = models.DateTimeField('Date', default=timezone.now)

    def __str__(self):
        return self.comment_text[:10]







