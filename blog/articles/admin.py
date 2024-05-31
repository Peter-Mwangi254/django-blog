from django.contrib import admin
from .models import Article, Comment

admin.site.register(Article)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created', 'active']
    list_filter = ['active', 'created']
    search_fields = ['post__title', 'author__username', 'text']
    actions = ['approve_comments']