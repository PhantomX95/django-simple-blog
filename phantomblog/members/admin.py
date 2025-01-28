from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'profile_pic')
    list_filter = ('location',)
    search_fields = ['user__username', 'user__email']