from django.core.checks import messages
from board.models import Post
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404

def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'like':
        post_list = Post.objects.annotate(num_liked=Count('liked')).order_by('-num_liked', '-create_date')
    elif so == 'comment':
        post_list = Post.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    elif so == 'hit':
        post_list = Post.objects.order_by('-hits', '-create_date')
    else:  # recent
        post_list = Post.objects.order_by('-create_date')

    if kw:
        post_list = post_list.filter(
            Q(subject__icontains=kw)|
            Q(content__icontains=kw)|
            Q(author__username__icontains=kw)|
            Q(comment__author__username__icontains=kw)
        ).distinct()

    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)

    context = {'post_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'board/post_list.html', context)

def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except:
        
        return redirect('board:index')
    #post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'board/post_detail.html', context)
