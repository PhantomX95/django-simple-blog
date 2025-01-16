from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on', 'updated_on', )
    list_filter = ('status', 'author', 'created_on', 'updated_on')
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)