from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import ModelFormMixin
from .models import Blog, Category, Comment, Post
from .forms import CommentCreateFrom


class TopView(generic.ListView):
    """
    トップページの記事を表示
    """

    model = Post
    template_name = 'cuba/index.html'


class IndexView(generic.ListView):
    """
    Blogの記事を表示。1ページに3つの記事を表示する。
    """
    model = Blog
    paginate_by = 3

    def get_queryset(self):
        """
        記事を投稿順に表示
        """
        queryset = Blog.objects.order_by('-created_at')

        return queryset


class CategoryView(generic.ListView):
    """
    カテゴリーを表示。カテゴリーで絞って1ページに3つまでの記事を表示する。
    """
    model = Blog
    paginate_by = 3

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Blog.objects.order_by('-created_at').filter(category=category)
        return queryset


class DetailAndCreateView(ModelFormMixin, generic.DetailView):
    """
    1つずつの記事に投稿フォームを作成し表示する。
    """
    model = Blog
    form_class = CommentCreateFrom
    template_name = 'cuba/blog_detail.html'

    def form_valid(self, form):
        """
        フォームに入力された内容が正しいかチェックし、登録後に詳細ページを表示へ。
        """
        post_pk = self.kwargs['pk']
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Blog, pk=post_pk)
        comment.save()
        return redirect("cuba:detail", pk=post_pk)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.object = self.get_object()
            return self.form_invalid(form)


def about(request):
    return render(request, 'cuba/about.html')
