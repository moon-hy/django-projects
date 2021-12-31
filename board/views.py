from django.core.checks import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.utils import timezone
from django.views import generic
from django.core.paginator import Paginator
from board.forms import CommentForm, QuestionForm
from board.models import Question, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-create_date')

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'board/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'board/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, 'Permission error.')
        return redirect('board:detail', question_id=question_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('board:detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)
    context = {'form':form}
    return render(request, 'board/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, 'Permission error.')
        return redirect('board:detail', question_id=question_id)
    question.delete()
    return redirect('board:index')

@login_required(login_url='common:login')
def comment_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            question.comment_set.create(
                author=request.user,
                content=request.POST.get('content'),
                create_date=timezone.now()
            )
            return redirect('board:detail', question_id=question_id)
    else:
        form = CommentForm()
    context = {'question': question, 'form':form}
    return render(request, 'board/question_detail.html', context)

@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, 'Permission error.')
        return redirect('board:detail', question_id=comment.question.id)
    comment.delete()
    return redirect('board:detail', question_id=comment.question.id)

'''
# When user generic: 
class IndexView(generic.ListView):
    def get_queryset(self):
        return Question.objects.order_by('-create_date')

class DetailView(generic.DetailView):
    model = Question
'''
