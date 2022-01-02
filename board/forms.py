from django import forms
from django.forms import widgets
from board.models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content']
        labels = {
            'subject': 'Subject',
            'content': 'Content',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels ={
            'content': 'Content',
        }