from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.checks import messages
from board.models import Post, Comment, Notification, User
from board.forms import CommentForm

@login_required(login_url='common:login')
def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            now = timezone.now()

            comment = Comment(post=post, author=request.user, content=request.POST.get('content'), create_date=now)
            comment.save()
            
            Notification(user=post.author, post=post, comment=comment, create_date=now).save()
            # 수정 postgresql migrate -> distinct on 가능
            activities = Comment.objects.filter(post=post)\
                .exclude(author__in=[request.user,post.author])\
                    .distinct('author')\
                        .select_related('author')

            for activity in activities:
                Notification(user=activity.author, post=post, comment=comment, create_date=now).save()

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
