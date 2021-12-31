from django.contrib import admin
from .models import Comment, Question
# Register your models here.

@admin.register(Question,Comment)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']

#admin.site.register(Question, QuestionAdmin)