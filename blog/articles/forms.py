from django import forms
from .models import Article, Comment

class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'thumb',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']