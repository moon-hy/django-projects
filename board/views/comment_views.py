from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.checks import messages
from board.models import Post, Comment
from board.forms import CommentForm

@login_required(login_url='common:login')
def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post.comment_set.create(
                author=request.user,
                content=request.POST.get('content'),
                create_date=timezone.now()
            )
            return redirect('board:detail', post_id=post_id)
    else:
        form = CommentForm()
    context = {'post': post, 'form':form}
    return render(request, 'board/post_detail.html', context)

@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, 'Permission error.')
        return redirect('board:detail', post_id=comment.post.id)
    comment.delete()
    return redirect('board:detail', post_id=comment.post.id)

@login_required(login_url='common:login')
def comment_like(request, comment_id):
    pass

@login_required(login_url='common:login')
def comment_dislike(request, comment_id):
    pass

