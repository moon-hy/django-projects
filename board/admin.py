from django.contrib import admin
from .models import Answer, Question
# Register your models here.

@admin.register(Question,Answer)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']

#admin.site.register(Question, QuestionAdmin)