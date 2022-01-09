from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from board.models import Category, Post
from board.forms import PostForm



@login_required(login_url='common:login')
def post_create(request, category_url):
    if request.method == 'POST':
        form = PostForm(request.POST)
        category = Category.objects.get(url=category_url)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category = category
            post.create_date = timezone.now()
            post.save()
            return redirect('board:category', category.url)
    else:
        form = PostForm()
    context = {'form': form}
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
    if request.user in post.disliked.all():
        messages.error(request, "이미 비추천에 투표하였습니다.")
    else:
        if request.user in post.liked.all():
            post.liked.remove(request.user)
        else:
            post.liked.add(request.user)
    return redirect('board:detail', post_id=post_id)

@login_required(login_url='common:login')
def post_dislike(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user in post.liked.all():
        messages.error(request, "이미 추천에 투표하였습니다.")
    else:
        if request.user in post.disliked.all():
            post.disliked.remove(request.user)
        else:
            post.disliked.add(request.user)
    return redirect('board:detail', post_id=post_id)

