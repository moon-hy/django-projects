from django import forms
from django.forms import widgets
from board.models import Comment, Post, Notification
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content']
        labels = {
            'subject': 'Subject',
            'content': 'Content',
        }
        widgets = {
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '500px'}}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels ={
            'content': 'Content',
        }
