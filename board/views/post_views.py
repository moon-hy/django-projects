from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from board.models import Post
from board.forms import PostForm



@login_required(login_url='common:login')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            post.save()
            return redirect('board:index')
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'board/post_create_form.html', context)

@login_required(login_url='common:login')
def post_modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, 'Permission error.')
        return redirect('board:detail', post_id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modify_date = timezone.now()
            post.save()
            return redirect('board:detail', post_id=post_id)
    else:
        form = PostForm(instance=post)
    context = {'form':form}
    return render(request, 'board/post_create_form.html', context)

@login_required(login_url='common:login')
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, 'Permission error.')
        return redirect('board:detail', post_id=post_id)
    post.delete()
    return redirect('board:index')

@login_required(login_url='common:login')
def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # 이미 추천을 했으면 못하게 해야함 
    # ManyToManyField는 중복 허용하지 않는다고 한다.
    # if request.user in post.liked.user_set 필요없음
    if request.user in post.liked.all():
        messages.error(request, 'You already liked this post')
    else:
        post.liked.add(request.user)
    return redirect('board:detail', post_id=post_id)

@login_required(login_url='common:login')
def post_dislike(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user in post.disliked.all():
        messages.error(request, 'You already disliked this post')
    else:
        post.disliked.add(request.user)
    return redirect('board:detail', post_id=post_id)

