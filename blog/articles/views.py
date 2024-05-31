from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

@login_required(login_url="/accounts/login/")
def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            # new_comment.post = article
            new_comment.author = request.user
            new_comment.save()
            return redirect('articles:article_detail', slug=article.slug)
    else:
        comment_form = CommentForm(initial={'post': article.id})

    return render(request, 'articles/article_detail.html', {'article': article,
                                                            'comments': comments,
                                                            'new_comment': new_comment,
                                                            'comment_form': comment_form})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:article_list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', { 'form': form })