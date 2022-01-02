from django.urls import path

from .views import base_views, comment_views, post_views

app_name = 'board'

urlpatterns = [
    # base_views.py
    path('', 
        base_views.index, name='index'),
    path('post/<int:post_id>/', 
        base_views.detail, name='detail'),
    # When use generic
    #path('<int:pk>/', views.DetailView.as_view()),

    # comment_views.py
    path('comment/create/<int:post_id>/', 
        comment_views.comment_create, name='comment_create'),
    path('comment/delete/<int:comment_id>/', 
        comment_views.comment_delete, name='comment_delete'),

    # post_views.py
    path('post/create/',
        post_views.post_create, name='post_create'),
    path('post/modify/<int:post_id>/', 
        post_views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>/', 
        post_views.post_delete, name='post_delete'),
    path('post/like/<int:post_id>/',
        post_views.post_like, name='post_like'),
    path('post/dislike/<int:post_id>/',
        post_views.post_dislike, name='post_dislike'),

]
