from django import forms
from .models import Article, Comment

class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'thumb',]

class CommentForm(forms.ModelForm):
    post = forms.ModelChoiceField(queryset=Article.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ['post', 'text']