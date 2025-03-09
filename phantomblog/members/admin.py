from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'profile_pic', 'is_writer')
    list_filter = ('location', 'is_writer')
    search_fields = ['user__username', 'user__email']
    list_editable = ('is_writer',)