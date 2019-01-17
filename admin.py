from django.contrib import admin
from .models import Blog, Category, Comment, Post

admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)