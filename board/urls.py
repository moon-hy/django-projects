from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    # When use generic
    #path('<int:pk>/', views.DetailView.as_view()),
    path('comment/create/<int:question_id>/', views.comment_create, name='comment_create'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),

]
