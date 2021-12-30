from django import forms
from django.forms import widgets
from board.models import Answer, Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': 'Subject',
            'content': 'Content'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels ={
            'content': 'Content',
        }