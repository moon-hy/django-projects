from django.contrib import admin
from .models import Comment, Post, Category
# Register your models here.

@admin.register(Post,Comment)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']

admin.site.register(Category)
#admin.site.register(Post, PostAdmin)