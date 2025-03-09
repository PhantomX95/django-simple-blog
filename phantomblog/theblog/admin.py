from django.contrib import admin
from .models import Post, Category, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on', 'updated_on')
    list_editable = ('status',)
    list_filter = ('status', 'author', 'created_on', 'updated_on')
    search_fields = ['title', 'content']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ['name', 'slug']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'body')
    list_filter = ('author',)
    search_fields = ['author', 'body']

