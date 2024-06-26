from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='home'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/create/', views.article_create, name='article_create'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('', include('django.contrib.auth.urls')),
]
