from os import X_OK
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.paginator import Paginator

from board.models import Post, Comment, Notification

def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    posts = Post.objects.filter(author=user).order_by('-create_date')
    comments = Comment.objects.filter(author=user).order_by('-create_date')
    agg = {'liked_sum': posts.aggregate(Sum('liked'))['liked__sum'],
            'disliked_sum': posts.aggregate(Sum('disliked'))['disliked__sum']}

    posts = Paginator(posts, 10).get_page(1)
    comments = Paginator(comments, 10).get_page(1)

    context = {'user':user, 'posts':posts, 'comments':comments, 'agg':agg}
    return render(request, 'board/user_profile.html', context)

def user_notification(request, user_id):
    user = User.objects.get(pk=user_id)
    notifications = Notification.objects.filter(user=user).order_by('read_date','-create_date')
    #notifications = Notification.objects.filter(user=user).filter(read_date__isnull=True).order_by('-read_date','-create_date')
    context = {'user': user, 'notifications': notifications}
    return render(request, 'board/user_notification.html', context)
