from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.utils import timezone
from django.views import generic
from django.core.paginator import Paginator
from board.forms import AnswerForm, QuestionForm
from board.models import Question, Answer

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

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            question.answer_set.create(
                content=request.POST.get('content'),
                create_date=timezone.now()
            )
            '''
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            '''
            return redirect('board:detail', question_id=question_id)
        else:   
            return HttpResponseRedirect(resolve_url('board:detail', question_id))

    else:
        form = AnswerForm()
    context = {'question': question, 'form':form}
    return render(request, 'board/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'board/question_form.html', context)

'''
# When user generic: 
class IndexView(generic.ListView):
    def get_queryset(self):
        return Question.objects.order_by('-create_date')

class DetailView(generic.DetailView):
    model = Question
'''
