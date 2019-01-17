from django.test import TestCase
from django.urls import reverse

from . models import Category, Blog, Comment


class TestIndex(TestCase):
    def test_get(self):
        res = self.client.get(reverse('cuba:index'))
        self.assertTemplateUsed(res, 'cuba/index.html')


class TestBlog(TestCase):
    def test_get(self):
        category = Category.objects.create(name='カテゴリー1')
        Blog.objects.create(title="タイトル1", text="テキスト1", category=category)
        Blog.objects.create(title="タイトル2", text="テキスト2", category=category)

        res = self.client.get(reverse('cuba:blog'))
        self.assertTemplateUsed(res, 'cuba/blog_list.html')
        self.assertContains(res, 'タイトル1')
        self.assertContains(res, 'タイトル2')
        self.assertContains(res, 'テキスト1')
        self.assertContains(res, 'テキスト2')
        self.assertContains(res, 'カテゴリー1')


class TestAbout(TestCase):
    def test_get(self):
        res = self.client.get(reverse('cuba:about'))
        self.assertTemplateUsed(res, 'cuba/about.html')


class TestDetailComment(TestCase):
    pass





