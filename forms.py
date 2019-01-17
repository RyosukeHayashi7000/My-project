from django import forms

from .models import Comment


class CommentCreateFrom(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'comment_text')